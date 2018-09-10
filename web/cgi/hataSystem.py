#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
   ProjectHata用振動子シーケンサー管理用プログラム
'''

import cgi, cgitb
import csv
import os
import glob
import thisis

cgitb.enable()  #CGIプログラムのデバッグ用：詳細 http://www.gesource.jp/programming/python/cgi/0116.html
form = cgi.FieldStorage()

# 実行環境がRaspberryPIかそうでないかを判定
if thisis.PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''

# FNにcsvのファイル名をセット
PLIST = "PList.csv"
FN = path + PLIST


def txtFileRead(fn):
    """テキストファイル読み込み"""
    with open(fn, 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
        s = f.read()
    return(s)

# HTMLテキストを作成、表示部
html_body0 = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv=”Cache-Control” content=”no-cache”>
<title>ProjectHata Vibration Sequencer</title>

<link rel="stylesheet" type="text/css" href="../css/html5reset-1.6.1.css"  />
<link rel="stylesheet" type="text/css" href="../css/btn.css"  />
<script type="text/javascript" src="https://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript" src="../js/js.js"></script>

<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<hr/>

"""

print("Content-Type: text/html;charset=ISO-2022-JP\n")
print(html_body0)

# CSVファイルを取り込み
rl=txtFileRead(FN)

#rlは全体文字列なので行ごとに分割してList化
lines=rl.splitlines()

#csvの1行めはRUN/STOP,フレームSec
# ---仕様変更。スタート＆ストップはstartstop.datで確認

with open(path + 'startstop.dat','r') as ssf:
    sss = ssf.read()
    #print('SSS=',sss)
    wk_status=int(sss.strip())
#print('wk_status:',wk_status)
l1=lines[0].split(',')
#wk_status=l1[0]
wait_time=float(l1[0])

print('<div>')
print('MODE:')
print('<input type="text" id="stat" name="stat" size=6')
print('value="')
if wk_status==1 :
    print('PLAY')
else:
    print('STOP')

print('">') #textbox閉じる
print('<form action="ssDatCng.py">')
print('<input id="PlayStopBtn" type="submit" value="Play/Stop" /><br />')
print('</form>')

print('<br/>')
print('<br/>WaitTime:')
print('<input type="text" id="WaitTime" name="WaitTime" size=6 onKeyUp="waitTextValueCng(this)" ')
print('value="')

print(wait_time)
print('">') #textbox閉じる
print('sec')

print('</div>')

#２行目以降
for i in range(1,7):
    #print(i,lines[i],'<br>')
    pos=lines[i].split(',')
    for jn,j in enumerate(pos):
        #print('<button type="button" class="btn" name="1-01"> </button>')
        #nmStr=str(i)+'-'+'{0:02d}'.format(j)
        nmStr=str(i)+'-'+str(jn+1)
        act=' '
        if j == '1':
            act=' active'
        btntxt='<button type="button" class="btn%s" name="%s"> </button>' % (act, nmStr)
        print(btntxt)
    print("<br/>")

print("<hr/>")


html_body1="""
<form action="CGItoCSV.py" method="POST">
 <textarea id="dataview" name="text" rows="8" cols="42">%s</textarea>
 <input type="submit" name="submit" value="DataSend"/>
</form>
<hr/>

"""
print(html_body1 % (rl))
#print(rl)


html_body2="""
PRE-SET: <input type="submit" value="EMA.csv" onclick="cpFileBtnOn(this)" /> <input type="submit" value="WAVE.csv" onclick="cpFileBtnOn(this)"/>
<input type="submit" value="all_0.csv" onclick="cpFileBtnOn(this)"/> <input type="submit" value="all_1.csv" onclick="cpFileBtnOn(this)"/>
<input type="submit" value="PList0.csv" onclick="cpFileBtnOn(this)"/>
<form action="fileCpy.py" method="POST">
 <input type="text" id="csvFileNameText" name="inCSVFile" size="30" value="%s">

 <input type="submit" name="csvCp" value="CSV LOAD"/>
</form>

<hr/>
"""

rl='PList0.csv'
#print(html_body2 % (rl))


#[r.split('/')[-1] for r in glob.glob('test/*')]
csvList=[r.split('/')[-1] for r in glob.glob(path + "*.csv")]

csvList.remove(FN)

print('Preset Pattern CSV List<br/>')
print('<select id="listbox" size="5" />')
#print('<select id="listbox" size="5"  />')

for lst in csvList:
    print('  <option value="%s">%s</option>' % (lst,lst))
print('</select>')


html_body2="""
<form action="fileCpy.py" method="POST">
 <input type="text" id="csvFileNameText" name="inCSVFile" size="30" value="%s">

 <input type="submit" name="csvCp" value="LOAD"/>
</form>

<hr/>
"""
print(html_body2 % (csvList[0]))

print("<hr/></body></html>")
