#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: length-of-last-word.py

@time: 2018/4/17 0017 23:15

@desc:
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。
'''


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    tmp_list = s.strip().split(" ")
    l = len(tmp_list)
    if l == 0:
        return 0
    else:
        return len(tmp_list[-1])

if __name__ == '__main__':
    s = "a "
    print lengthOfLastWord(s)

