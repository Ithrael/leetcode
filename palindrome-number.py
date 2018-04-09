#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: palindrome-number.py

@time: 2018/4/9 0009 22:42

@desc:
'''


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    x = str(x)
    l = len(x)
    for i in range(l/2):
        if x[i]!=x[-1-i]:
            return False
    return True

if __name__ == '__main__':
    input = 12333333333333333333333333333333210
    print isPalindrome(input)