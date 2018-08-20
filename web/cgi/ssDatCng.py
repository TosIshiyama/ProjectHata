#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

with open('startstop.dat', 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
    s = f.read()

startstopFlg = int(s.strip())

ss=''
if startstopFlg == 1:
    with open('startstop.dat', 'w') as f:
        f.write('0')
    ss='STOP Changed'
else:
    with open('startstop.dat', 'w') as f:
        f.write('1')
    ss='PLAY Changed'

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>PLAY/STOP change</title>
<meta http-equiv="refresh"content="0; url=HataSystem.py"> <!-- 自動でページ戻り -->
</head>
<body>
%s
</body>
</html>
"""

print(html_body % (ss))
