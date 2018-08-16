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
</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','')

with open('test.csv','w') as f:
    f.write(text)

print(html_body % (text))
