# ProjectHata

# RaspberryPiで動作する振動アクチュエータドライバ

## 目的
* パーキンソン病の方が意図せず指先が震えてしまう現象を是正したい。

## 設計
* 腕に巻いたバンドにセットされた振動アクチュエータを特定のパターンで振動させることによって、脳と指先の間の神経伝達フィードバックをジャミングできる（らしい？）→成功例あり(?)  http://www.itmedia.co.jp/news/articles/1705/11/news098.html  


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
* pythonは3環境用。
* Windowsではデバッグ用にサーバーを立ち上げ、GPIOアクセスはしない状態でテスト動作するようにした。
  * Windows環境では、/web/で python3 cgiserver.py を実行しておくと、以後、ブラウザから localhost:8000/ でアクセスできる。hataSystemへは http://localhost:8000/cgi/hataSystem.py でアクセス可。(web/でcgiserver.pyを立ち上げているので。)  

* web/cgi/thisis.py というスクリプト内のPI=FalseでWin環境、TrueでPI環境となる。(web/thisis.pyはcgi以下からのシンボリックリンク)
  * web/hataLoop.pyは、スクリプト冒頭の PI=False を TrueにすればRaspberryPi上で実行されているとみなしてGPIOにアクセス（RaspberryPiモード）になる。Falseではデバッグ用プリントのみ。
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

### 自動実行について
pi@raspberrypi:~ $ cat /home/pi/start.sh  
#!/bin/sh  
cd /home/pi/ProjectHata/web  
sudo i2cset -y 1 0x19 0x20 0x27 b  
sudo i2cset -y 1 0x18 0x20 0x27 b  
python3 hataLoop.py &  

↑このスクリプトを/etc/rc.local から呼び出し、電源投入後自動起動するようにした。参考：http://hendigi.karaage.xyz/2016/11/auto-boot/



### output.dat について
output.datに３軸センサからの入力値を記録する（追加上書き）  
データ内容は以下の通り（csv風）
＞date&time(ミリ秒), a(アクチュエータ)1のON/OFF,a2,a3,a4,a5,a6,センサch1_x,ch1_y,ch1_z,センサch2_x,ch2_y,ch2_z  
↓サンプル  
2018-09-07 12:46:51.853485,1,1,1,0,1,0,279.91, 357.19, -122.50,-700.09, -419.92, -1489.14  
2018-09-07 12:46:52.060986,1,0,0,0,1,0,283.73, 357.19, -122.50,-692.44, -419.92, -1492.97  
2018-09-07 12:46:52.267392,1,1,1,1,0,1,272.25, 357.19, -114.84,-703.92, -419.92, -1496.80  
2018-09-07 12:46:52.473584,1,0,0,0,1,1,279.91, 361.02, -118.67,-700.09, -419.92, -1500.62  
2018-09-07 12:46:52.679546,1,1,1,1,0,1,283.73, 357.19, -130.16,-711.58, -416.09, -1492.97  
2018-09-07 12:46:52.901875,0,1,1,1,1,1,279.91, 361.02, -130.16,-711.58, -419.92, -1500.62  
2018-09-07 12:46:53.111465,1,1,0,0,0,1,279.91, 357.19, -122.50,-707.75, -396.95, -1427.89  
2018-09-07 12:46:53.320931,1,0,1,1,1,1,276.08, 357.19, -114.84,-700.09, -427.58, -1496.80  




### outtail.sh について  
outtail.shは、たまっていくoutput.datの整理用シェルスクリプト。output.datの末尾５００行のみを残し、前のほうはカットする。  
crontab で１時間ごとに自動起動するようにするとよい  
crontab -l   
0 * * * * /home/pi/ProjectHata/outtail.sh  
↑こんなかんじで(cronの実行はRaspberryPiでは自動実行されていないことがあるので注意 $ sudo /etc/init.d/cron start で起動)  

### 加速度センサLISD3DHについて  
参考：https://qiita.com/sh8/items/d48488c7ae8817de6074  
pi@raspberrypi:~/ProjectHata $ sudo i2cdetect -y 1  
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f  
00:          -- -- -- -- -- -- -- -- -- -- -- -- --  
10: -- -- -- -- -- -- -- -- 18 19 -- -- -- -- -- --  
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
70: -- -- -- -- -- -- -- --  
↑18と19の2chを使用する  

> $ sudo i2cget -y 1 0x19 0x0f b  
`0x33`  
> $ sudo i2cget -y 1 0x18 0x0f b  
`0x33`  
↑で接続確認（0x33が帰る）  

> $ sudo i2cset -y 1 0x19 0x20 0x27 b  
> $ sudo i2cset -y 1 0x18 0x20 0x27 b  

↑これでEnabele。（必要）
