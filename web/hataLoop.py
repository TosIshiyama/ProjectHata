#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" RaspberryPi 上でシーケンサーループさせる """

PI=True

if PI: import RPi.GPIO as GPIO

if PI:
    path='/home/pi/ProjectHata/web/'
else:
    path=''


import time
import csv
import os

import pdb

GPIO4 = 7   #　GPIO番号＝PIN番号
GPIO14 = 8
GPIO15 = 10
GPIO17 = 11
GPIO18 = 12
GPIO27 = 13

DPL = [GPIO4,GPIO14,GPIO15,GPIO17, GPIO18, GPIO27]   #使用するデジタルポートリスト

Fn = path+'PList.csv'    #決め打ち
datFn = path+'startstop.dat'

tms0=0  #タイムスタンプリセット
tmsd0=0  #タイムスタンプリセット


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

if PI: GpioInit()

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
            if PI: DLinePut(pl)
            #time.sleep(0.1)  #100ms Wait
            time.sleep(waitSec)
            print(pl)
    else:
        if PI: DLinePut([0,0,0,0,0,0])
