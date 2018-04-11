#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangchong

@contact: wh01096045@163.com

@file: array1.py

@time: 2018/4/11 0011 21:06

@desc:
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。

不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。
'''


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    if l == 0:
        return 0
    index = 0
    for i in range(l):
        if nums[i]!=nums[index]:
            index += 1
            nums[index]=nums[i]
    index += 1
    return index


if __name__ == '__main__':
    nums = [0,1,1,2,2,3,3,4]
    print removeDuplicates(nums)
