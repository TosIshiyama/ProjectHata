#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus
import time
import math

i2c = smbus.SMBus(1)
address = 0x19

# 平常時のX軸、Y軸の値が0になるように下記の値を修正してください
default_x_a = 25.0
default_y_a = 8.0

def s18(value):
    return -(value & 0b100000000000) | (value & 0b011111111111)

while True:

    x_l = i2c.read_byte_data(address, 0x28)
    x_h = i2c.read_byte_data(address, 0x29)
    print(x_l,x_h)
    x_a = (x_h << 8 | x_l) >> 4
    x_a = s18(x_a)/1024.0*980.0 - default_x_a
    print("X-Value:%6.2f" % (x_a))

    y_l = i2c.read_byte_data(address, 0x2A)
    y_h = i2c.read_byte_data(address, 0x2B)
    y_a = (y_h << 8 | y_l) >> 4
    y_a = s18(y_a)/1024.0*980.0 - default_y_a
    print("Y-Value:%6.2f" % (y_a))

    z_l = i2c.read_byte_data(address, 0x2C)
    z_h = i2c.read_byte_data(address, 0x2D)
    z_a = (z_h << 8 | z_l) >> 4
    z_a = s18(z_a)/1024.0*980.0
    print("Z-Value:%6.2f" % (z_a))

    gal = math.hypot(x_a, y_a)
    print("Gal:%6.2f" % (gal))

    time.sleep(1)

