#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータ</title>
</head>
<body>
%s<br>
を保存しました。
<A HREF="hataSystem.py">戻る</A>
</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','')

# 読み込んだ文字列のCR(\r)を削除する。 # Windowsだと勝手にCRLFになってしまうので対策
txt = text.replace('\r', '')


#with open('test.csv','w') as f:
#with open('PList.csv','w') as f:
#    f.write(text)

# ファイルをバイナリモードで開く
with open('PList.csv', 'wb') as a_file:
  # 文字列をバイト列にして保存する
  a_file.write(txt.encode('utf-8'))


print(html_body % (text))
