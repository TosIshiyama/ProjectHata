#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータテスト表示</title>
<meta http-equiv="refresh"content="0; url=HataSystem.py"> <!-- 自動でページ戻り -->
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

# 以下、Windowsでの実行対策：読み込んだ文字列のCR(\r)を削除する。（Windowsだと勝手にCRLFになってしまうので。）
txt = text.replace('\r', '')

# ファイルをバイナリモードで開く
with open('PList.csv', 'wb') as a_file:
  # 文字列をバイト列にして保存する
  a_file.write(txt.encode('utf-8'))


print(html_body % (text))
