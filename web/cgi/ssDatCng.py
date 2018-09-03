#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' START／STOP ボタンを押した時に呼ばれる
 startstop.dat の内容を0－＞１ ／　1-＞０にトグルチェンジする
'''

import os
import thisis


#PI=True

if thisis.PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''

with open(path+'startstop.dat', 'r') as f:
    s = f.read()

startstopFlg = int(s.strip())

ss=''
if startstopFlg == 1:
    with open(path+'startstop.dat', 'w') as f:
        f.write('0')
    ss='Changed to [STOP]'
else:
    with open(path+'startstop.dat', 'w') as f:
        f.write('1')
    ss='Changed to [PLAY]'

# Webページ表示０秒後にhataSystem.pyを再度呼び出す
html_body = """
<!DOCTYPE html>
<html>
<head>
<title>PLAY/STOP change</title>
<meta http-equiv="refresh"content="0; url=hataSystem.py">
</head>
<body>
%s
</body>
</html>
"""
print("Content-type: text/html")
print(html_body % (ss))
