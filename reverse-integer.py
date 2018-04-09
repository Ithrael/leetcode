#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: reverse-integer.py

@time: 2018/4/9 0009 21:38

@desc:
'''
import math

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    a = x
    if x<0:
        x = -x
    nums = []
    while(x!=0):
        y = x % 10
        x = x / 10
        nums.append(y)
    l = len(nums)
    sum = 0
    for i in range(l):
        sum+=nums[i]*(10**(l-i-1))
    if sum > 2**31:
        return 0
    if a < 0:
        return -sum
    return sum

if __name__ == '__main__':
    input = 1563847412
    print reverse(input)