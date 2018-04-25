#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: remove-element.py

@time: 2018/4/25 0025 23:52

@desc:
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = 0
    length = len(nums)
    for i in range(length-1):
        if nums[i] == val:
            l += 1
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
    print nums
    return l

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print removeElement(nums, val)