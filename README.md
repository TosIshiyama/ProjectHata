# ProjectHata

# RaspberryPiで動作する振動アクチュエータドライバ

## 目的
* パーキンソン病の方が意図せず指先が震えてしまう現象を是正したい。

## 設計
* 腕に巻いたバンドにセットされた振動アクチュエータを特定のパターンで振動させることによって、脳と指先の間の神経伝達フィードバックをジャミングできる（らしい？）→成功例あり


## プログラム仕様
* pythonでcgiを作成、Web上からアクチュエータ振動パターンをデザインできるようにする

## 実装
* HTMLもPython（cgi）から自動生成して表示
  * /web/cgi/hataSystem.py
* シーケンスデータの編集はJavaScriptでリアルタイム編集できるようにした
  * /js/js.js
* 実際の動作部もpythonのスクリプトとし、RaspberryPi上で実行、GPIO制御で振動アクチュエータをドライブする。
  * /web/hataLoop.py

## 基本構成ブロック図
https://github.com/TosIshiyama/ProjectHata/blob/master/ProjectHataBlockDiagram.pdf

## ダウンロードと環境設定
https://github.com/TosIshiyama/ProjectHata  
からzipをダウンロードするか、  
コンソールより  
> git clone https://github.com/TosIshiyama/ProjectHata  

でプロジェクト全体をクローンする。  

* pythonスクリプトをCGIで実行可に
> chmod 755 *.py  

* csv ファイルとdatを書き込み可に
> chmod 666 *.csv  
> chmod 666 *.dat  

* thisis.py をweb/ と web/cgi以下に作成。内容は
> PI = True  

または　　
> PI = False  

とする。(TrueでRaspberryPi、FalseでWindows環境を想定）
----
## 環境と動作
* デバッグ用にWindowsでサーバーを立ち上げ、GPIOアクセスはしない状態でテスト動作するようにした。
  * cgi/thisis.py というスクリプト内のPI=FalseでWin環境、TrueでPI環境となる。
  * web/hataLoop.pyは、スクリプト冒頭の PI=False を TrueにすればRaspberryPi上で実行されているとみなしてGPIOにアクセス（RaspberryPiモード）になる。Falseではデバッグ用プリントのみ。
  * Windows環境では、/web/で python3 cgiserver.py を実行しておくと、以後、ブラウザから localhost:8000/ でアクセスできる。hataSystemへは localhost:8000/web/cgi/hataSystem.py でアクセス可。
  * RaspberryPiにはApache2がセットアップされている、pythonスクリプトをCGIで実行可に。
  * pi上からはlocalhost/web/cgi/hataSystem.py でWebからの操作ができる。
  * なお、現在のRaspberryPiは研究室LANのローカルアドレス： 10.18.51.0 にあり。 http://10.18.51.0/web/cgi/hataSystem.py で、同一LAN環境からは別PCからでもアクセス可
* メインプログラムのループは web/hataLoop.pyにあり、 pyhton3 hataLoop.py　を予め実行しておく。
  * raspberryPi上では /ProjectHata/web/hataLoop.py

----

### パターンリストCSV仕様メモ
* LINE1> 1フレーム停止時間(s)
* LINE2～6> LINE-1チャンネルのON/OFF（1/0),,,～２０個

* PList.csv例

pi@raspberrypi:~/ProjectHata/py $ cat PList.csv  
0.2  
0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0  
0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0  
0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0  
0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0  
0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0  
0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0  

### startstop.dat
* 実行しているか止まっているかを1,0でセット

↑これらのファイルをhataLoop.pyで読み、実行する。

----

### メモ
