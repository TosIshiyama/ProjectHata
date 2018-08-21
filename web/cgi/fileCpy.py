#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import shutil
import cgi
import thisis

#PI=False

if thisis.PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''


form = cgi.FieldStorage()
text = form.getvalue('inCSVFile','')

#print(text)

shutil.copyfile(path+ text, path+"PList.csv")


html_body = """
<!DOCTYPE html>
<html>
<head>
<title>FileCopy change</title>
<meta http-equiv="refresh"content="1; url=hataSystem.py">
</head>
<body>
%s -> PList.csv
</body>
</html>
"""
print("Content-type: text/html")
print(html_body % (text))
