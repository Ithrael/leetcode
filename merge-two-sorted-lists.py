#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ithrael

@file: merge-two-sorted-lists.py

@time: 2018/4/13 0013 23:10

@desc:
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = []
    len1 = len(l1)
    len2 = len(l2)
    index1 = 0
    index2 = 0
    while True:

        if (l1[index1]<=l2[index2]):
            l3.append(l1[index1])
            index1+=1
        else:
            l3.append(l2[index2])
            index2+=1
        print index1, index2

        print l3
        if (index1==len1):
            index = len1
    return l3

if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    print mergeTwoLists(l1, l2)