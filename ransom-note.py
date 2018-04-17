#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: ransom-note.py

@time: 2018/4/17 0017 23:19

@desc:
赎金信
'''


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    for i in ransomNote:
        if magazine.__contains__(i):
            magazine = magazine.replace(i, "", 1)
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "ab"
    print canConstruct(ransomNote, magazine)
