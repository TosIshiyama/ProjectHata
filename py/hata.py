#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" RaspberryPi 上でシーケンサーループさせる """

#import wiringpi # GPIOを制御するライブラリ

import time
import csv
import os

GPIO4 = 7   #　GPIO番号＝PIN番号
GPIO14 = 8
GPIO15 = 10
GPIO17 = 11
GPIO18 = 12
GPIO27 = 13

DPL = [GPIO4,GPIO14,GPIO15,GPIO17, GPIO18, GPIO27]   #使用するデジタルポートリスト

Fn = 'PList.csv'

tms0=0  #タイムスタンプリセット

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
    wiringpi.digitalWrite( port, OnOff )

def DLinePut(DLine):
    '''６つのポートそれぞれをON/OFF'''
    for i,dp in enumerate(DPL):
        DigitalOnOff(dp,Dline[i])

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

while True:
    tms1=os.stat(Fn).st_mtime
    if tms0<tms1:
        print('File Updated:',tms1)
        tms0=tms1
        rl=csvRead(Fn)
        print(rl)

    for i in range(20):
        pl=LinePut(rl,i)
        #DLinePut(pl)
        time.sleep(0.1)  #100ms Wait
        print(pl)
