#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>aaa</title>
<meta http-equiv="refresh"content="0; url=hataSystem.py">
</head>
<body>
%s<br>
<A HREF="hataSystem.py">back</A>
</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','')

txt = text.replace('\r', '')

with open('/home/pi/ProjectHata/web/PList.csv', 'wb') as a_file:
  a_file.write(txt.encode('utf-8'))

print("Content-type: text/html")
print(html_body % (text))
