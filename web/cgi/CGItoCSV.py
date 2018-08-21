#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cgi

PI=True

if PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>CSV Updated</title>
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

with open(path+'PList.csv', 'wb') as a_file:
  a_file.write(txt.encode('utf-8'))

print("Content-type: text/html")
print(html_body % (text))
