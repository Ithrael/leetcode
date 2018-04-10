#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: search-insert-position.py

@time: 2018/4/10 0010 11:01

@desc:
'''


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = len(nums)
    for i in range(l):
        if nums[i] >= target:
            return i
    return l

if __name__ == '__main__':
    nums = [1,2,5,6]
    target = 7
    print searchInsert(nums, target)