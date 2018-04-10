#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: add-two-numbers.py

@time: 2018/4/9 0009 23:09

@desc:
'''


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    len1 = len(l1)
    # len2 = len(l2)
    result = []
    for i in range(len1):
        result.append(l1[len1-1-i]+l2[len1-1-i])
    return result

if __name__ == '__main__':
    l1 = [3,4,2]
    l2 = [4,6,5]
    print addTwoNumbers(l1, l2)