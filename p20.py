#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: p20.py

@time: 2018/4/14 0014 20:45

@desc:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    a = []
    for i in s:
        if i=="(" or i=="[" or i=="{":
            a.append(i)
        else:
            if len(a) == 0:
                return False
            if i==")":
                if a.pop()=="(":
                    continue
                else:
                    return False
            if i=="]":
                if a.pop()=="[":
                    continue
                else:
                    return False
            if i=="}":
                if a.pop()=="{":
                    continue
                else:
                    return False
    if len(a) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "("
    a = isValid(s)
    print a


