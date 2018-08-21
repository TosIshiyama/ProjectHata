#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import csv
import os
form = cgi.FieldStorage()

# Get data from fields
FN = form.getvalue('file')


def csvRead(fn):
    """テキストファイル読み込み"""
    with open(fn, 'r') as f:    #CGIの場合ドキュメントルートからのパスを確認すること！
        s = f.read()
    return(s)

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>ProjectHataシーケンサ</title>

<link rel="stylesheet" type="text/css" href="../css/html5reset-1.6.1.css"  />
<link rel="stylesheet" type="text/css" href="../css/btn.css"  />
<script type="text/javascript" src="https://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript" src="../js/js.js"></script>

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

<hr/>

//シーケンサーテスト
<div>
  <button type="button" class="btn" name="1-01"> </button>
  <button type="button" class="btn" name="1-02"> </button>
  <button type="button" class="btn" name="1-03"> </button>
  <button type="button" class="btn" name="1-04"> </button>
  <button type="button" class="btn" name="1-05"> </button>
  <button type="button" class="btn" name="1-06"> </button>
  <button type="button" class="btn" name="1-07"> </button>
  <button type="button" class="btn" name="1-08"> </button>
  <button type="button" class="btn" name="1-09"> </button>
  <button type="button" class="btn" name="1-10"> </button>
</div>

<div>
  <button type="button"  class="btn" name="2-01"> </button>
  <button type="button"  class="btn" name="2-02"> </button>
  <button type="button"  class="btn" name="2-03"> </button>
  <button type="button"  class="btn" name="2-04"> </button>
  <button type="button"  class="btn" name="2-05"> </button>
  <button type="button"  class="btn" name="2-06"> </button>
  <button type="button"  class="btn" name="2-07"> </button>
  <button type="button"  class="btn" name="2-08"> </button>
  <button type="button"  class="btn" name="2-09"> </button>
  <button type="button"  class="btn" name="2-10"> </button>
</div>
<hr>
<textarea id="dataview" name="dataview" cols="40" rows="6">
</textarea>

</body>
</html>
"""

#print ("Hello, %s!" % (FN, ))
#print (os.getcwd() )


rl=csvRead(FN)

print(html_body % (rl))
#print(rl)
