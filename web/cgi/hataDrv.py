#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import csv
import os

import cgitb

cgitb.enable()

form = cgi.FieldStorage()

# Get data from fields
FN = form.getvalue('file')


def txtFileRead(fn):
    """テキストファイル読み込み"""
    with open(fn, 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
        s = f.read()
    return(s)

html_body0 = """
<!DOCTYPE html>
<html>
<head>
<title>ProjectHataシーケンサ</title>

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

print(html_body0)

rl=txtFileRead(FN)

#rlは全体文字列なので行ごとに分割してList化
lines=rl.splitlines()

#csvの1行めはRUN/STOP,フレームSec
l1=lines[0].split(',')
wk_status=l1[0]
wait_time=float(l1[1])

print('<div>')
print('STATUS:')
print('<input type="text" id="stat" name="stat"')
print('value="')
if wk_status=='1':
    print('PLAY')
else:
    print('STOP')

print('">') #textbox閉じる
print(' / WaitTime:')
print('<input type="text" id="WaitTime" name="WaitTime"')
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
 <textarea name="text" rows="4" cols="40">%s</textarea>
 <input type="submit" name="submit" />

<hr/>
<textarea id="dataview" name="dataview" cols="40" rows="6">
</textarea>

"""
print(html_body1 % (rl))
#print(rl)

print("<hr/></body></html>")
