#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

with open('startstop.dat', 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
    s = f.read()

startstopFlg = int(s.strip())

if startstopFlg == 1:
    with open('startstop.dat', 'w') as f:
        f.write('0')
else:
    with open('startstop.dat', 'w') as f:
        f.write('1')

#ページ遷移入れる    
