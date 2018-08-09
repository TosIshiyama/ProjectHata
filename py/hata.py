#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" RaspberryPi 上でシーケンサーループさせる """

#import wiringpi # GPIOを制御するライブラリ

import time
import csv

GPIO4 = 7   #　GPIO番号＝PIN番号
GPIO14 = 8
GPIO15 = 10
GPIO17 = 11
GPIO18 = 12
GPIO27 = 13

DPL = [GPIO4,GPIO14,GPIO15,GPIO17, GPIO18, GPIO27]   #使用するデジタルポートリスト

#　サンプルデータ:テスト用
L0=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

L1=[1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

L2=[0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,
    0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,
    0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,
    0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,
    0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0]

def DigitalOnOff(port,OnOff):
    """デジタルポートをONまたはOFFさせる"""
    wiringpi.digitalWrite( led_pin, OnOff )

def GpioInit():
    # GPIO初期化
    wiringpi.wiringPiSetupGpio()
    # GPIOを出力モード（1）3.3v DigitalOutに設定
    for d in DPL:
        wiringpi.pinMode( d, 1 )

def LinePut(mlist,pos):
    """20*6のマトリクスを縦切りにしてpos列を取り出す"""
    p=[0,0,0,0,0,0]
    for i in range(6):
        pp=pos+i*20
        if pp>20*6:
            pp=pp-(20*6)
        p[i] = mlist[pp]
    return(p)

######################################

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

rl=csvRead('PList.csv')
print(rl)

print("---------------------")
while True:
    for i in range(20):
        pl=LinePut(rl,i)
        time.sleep(0.1)  #100ms Wait
        print(pl)
