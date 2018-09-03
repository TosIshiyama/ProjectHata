#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
   RaspberryPi 上でシーケンサーループさせる実行部
'''

import thisis   # thisis.pyは cgi以下に本体があるのでln -sでシンボリック・リンクしておく。

# 実行環境がRaspberryPIかそうでないかを判定、PI環境ならばGPIOをimport
if thisis.PI: import RPi.GPIO as GPIO

if thisis.PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''


import time
import csv
import os
import pdb

import smbus
import math


GPIO4 = 7   #　GPIO番号＝PIN番号
GPIO14 = 8
GPIO15 = 10
GPIO17 = 11
GPIO18 = 12
GPIO27 = 13

DPL = [GPIO4,GPIO14,GPIO15,GPIO17, GPIO18, GPIO27]   #使用するデジタルポートリスト

#File
Fn = path+'PList.csv'
datFn = path+'startstop.dat'
OutPutCSV = path+'output.dat'


tms0=0  #タイムスタンプリセット
tmsd0=0  #タイムスタンプリセット

# i2c　３軸センサー用
i2c = smbus.SMBus(1)
address = 0x19

# 平常時のX軸、Y軸の値が0になるように下記の値を修正してください
default_x_a = 25.0
default_y_a = 8.0

def s18(value):
    ''' ３軸センサ用 フィルタ'''
    return -(value & 0b100000000000) | (value & 0b011111111111)

def senserRead():
    ''' ３軸センサデータ読み込み＆出力'''
    x_l = i2c.read_byte_data(address, 0x28)
    x_h = i2c.read_byte_data(address, 0x29)
    #print(x_l,x_h)
    x_a = (x_h << 8 | x_l) >> 4
    x_a = s18(x_a)/1024.0*980.0 - default_x_a
    #print("X:%6.2f" % (x_a), end='')

    y_l = i2c.read_byte_data(address, 0x2A)
    y_h = i2c.read_byte_data(address, 0x2B)
    y_a = (y_h << 8 | y_l) >> 4
    y_a = s18(y_a)/1024.0*980.0 - default_y_a
    #print(" Y:%6.2f" % (y_a), end='')

    z_l = i2c.read_byte_data(address, 0x2C)
    z_h = i2c.read_byte_data(address, 0x2D)
    z_a = (z_h << 8 | z_l) >> 4
    z_a = s18(z_a)/1024.0*980.0
    #print(" Z:%6.2f" % (z_a), end='')

    gal = math.hypot(x_a, y_a)
    #print(" G:%6.2f" % (gal))

    ret='%6.2f, %6.2f, %6.2f' % (x_a,y_a,z_a)

    return(ret)

def DigitalOnOff(port,OnOff):
    """デジタルポートをONまたはOFFさせるON=True,OFF=False"""
    #wiringpi.digitalWrite( port, OnOff )
    sig=False
    if OnOff=='1': sig=True
    #print('On D OnOff:',port,sig)
    GPIO.output(port,sig)

def DLinePut(DLine):
    '''６つのポートそれぞれをON/OFF'''
    #print('DLinePut!',DLine)
    for i,dp in enumerate(DPL):
        DigitalOnOff(dp,DLine[i])


def GpioInit():
    # GPIO初期化
    GPIO.setmode(GPIO.BOARD) #BOARDはPIN番号指定
    #wiringpi.wiringPiSetupGpio()
    # GPIOを出力モード（1）3.3v DigitalOutに設定
    for d in DPL:
        #wiringpi.pinMode( d, 1 )
        print(d, end="")
        GPIO.setup(d, GPIO.OUT)
    print("")

def LinePut(mlist,pos):
    """20*6のマトリクスを縦切りにしてpos列を取り出す"""
    p=[0,0,0,0,0,0]
    for i in range(6):
        pp=pos+i*20
        if pp>20*6:
            pp=pp-(20*6)
        p[i] = mlist[pp +1 ]    #+1で冒頭のWaitTimeをカット
    return(p)


def csvRead(fn):
    """CSVファイル読み込み"""
    #with open('PList.csv', 'r') as f:
    with open(fn, 'r') as f:
        reader = csv.reader(f)
        rl=[]
        for row in reader:
            #print(row)
            rl.extend(row)

    return(rl)

######################################

if thisis.PI: GpioInit()

startstopFlg=0

while True:
    #タイムスタンプ確認
    tms1=os.stat(Fn).st_mtime
    tmsd1=os.stat(datFn).st_mtime
    if tms0<tms1:   #シーケンスデータが書き換わっていれば再読み込み
        print('File Updated:',tms1)
        tms0=tms1
        rl=csvRead(Fn)
        print(rl)

    if tmsd0<tmsd1:   #スタートストップフラグファイルが書き換わっているか確認
        print('START STOP File Updated:',tmsd1)
        tmsd0=tmsd1
        with open(datFn, 'r') as datf:    #CGIの場合ドキュメントルートからのパスを確認すること！
            sss = datf.read()
        startstopFlg = int(sss.strip())
        print(startstopFlg)


    if startstopFlg == 1:
        waitSec=float(rl[0])
        print("wait:",waitSec)
        for i in range(20):
            pl=LinePut(rl,i)
            if thisis.PI:
                DLinePut(pl)
                ans = senserRead()
                print(ans)
                mojiretu = ','.join(str_list) + ',' + ans
                with open(OutPutCSV, 'a') as of: # a = 追加書き込みモード
                    of.write(mojiretu)
            #time.sleep(0.1)  #100ms Wait
            time.sleep(waitSec)
            print(pl)
    else:
        if thisis.PI: DLinePut([0,0,0,0,0,0])
