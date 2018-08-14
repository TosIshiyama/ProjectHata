#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import csv
import os
form = cgi.FieldStorage()

# Get data from fields
FN = form.getvalue('file')


def csvRead(fn):
    """CSVファイル読み込み""" #これをテキスト読み込みにしたらいいんでは？
    #with open('PList.csv', 'r') as f:
    with open(fn, 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
    #with open('PList.csv', 'r') as f:
        reader = csv.reader(f)
        rl=[]
        for row in reader:
            #print(row)
            rl.extend(row)

    return(rl)

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータを表示</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<form action="CGItoCSV.py" method="POST">
 <textarea name="text" rows="4" cols="40">%s</textarea>
 <input type="submit" name="submit" />
</body>
</html>
"""

#print ("Hello, %s!" % (FN, ))
#print (os.getcwd() )


rl=csvRead(FN)

print(html_body % (rl))
#print(rl)
