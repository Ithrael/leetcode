#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: strStr.py

@time: 2018/4/18 0018 23:09

@desc:
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    if haystack.__contains__(needle):
        return haystack.index(needle)
    else:
        return -1
if __name__ == '__main__':
    haystack = ""
    needle = "a"
    print strStr(haystack, needle)