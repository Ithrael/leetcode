#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: p167.py

@time: 2018/4/10 0010 23:51

@desc:
'''

def twoSum(numbers, target):
    l = len(numbers)
    # index = 0
    # for i in range(l):
    #     if numbers[i] == target:
    #         index = i
    #         break
    m_index = l/2
    for i in range(l):
        for j in range(i+1, l):
            print i
            if numbers[i]+numbers[j]>target:
                break
            if numbers[i]+numbers[j]==target:
                return [i+1, j+1]


if __name__ == '__main__':
    numbers = [1,2,3,4]
    target = 6
    print twoSum(numbers, target)