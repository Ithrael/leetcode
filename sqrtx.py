#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: sqrtx.py

@time: 2018/4/10 0010 23:01

@desc:
'''
import math

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    return int(math.sqrt(x))

if __name__ == '__main__':
    print mySqrt(8)