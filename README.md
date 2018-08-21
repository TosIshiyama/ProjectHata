# ProjectHata

# RaspberryPiで動作する振動アクチュエータドライバ

## 目標
* py/ 以下の python3スクリプトでアクチュエータをドライブする
* web/ 以下でpython3 cgiを作成、Web上からアクチュエータ振動パターンをデザインできるようにする

----
* 各スクリプト冒頭の PI=False を TrueにすればRaspberryPi上で実行されているとみなしてGPIOにアクセス（RaspberryPiモード）になる。Falseではデバッグ用プリントのみ。
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

# メモ
* RaspberryPiでApache2をセットアップ、pythonスクリプトをCGIで実行可に。
* pi上からはlocalhost/web/cgi/hataSystem.py でWebからの操作ができる。
* なお、現在のRaspberryPiはローカルアドレス： 10.18.51.0 にあり。
http://10.18.51.0/web/cgi/hataSystem.py
でLAN環境からはアクセス可
