#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import csv
import os
form = cgi.FieldStorage()

# Get data from fields
FN = form.getvalue('file')


def csvRead(fn):
    """CSVファイル読み込み"""
    #with open('PList.csv', 'r') as f:
    with open(fn, 'r') as f:
    #with open('PList.csv', 'r') as f:
        reader = csv.reader(f)
        rl=[]
        for row in reader:
            #print(row)
            rl.extend(row)

    return(rl)


print ("Content-type:text/html\n\n")
print ("<html>")
print ("<head>")
print ("<title>Hello, world!</title>")
print ("</head>")
print ("<body>")

print ("Hello, %s!" % (FN, ))
print (os.getcwd() )

print ("<textarea>")


rl=csvRead(FN)
print(rl)

print ("</textarea>")



print ("</body>")
print ("</html>")
