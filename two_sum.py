#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: two_sum.py

@time: 2018/4/9 0009 21:22

@desc:
'''

def twoSum(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1,l):
            if nums[i]+nums[j] == target:
                return [i, j]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print twoSum(nums, target)