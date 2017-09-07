#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个链表，从尾到头打印链表每个节点的值。
返回从尾部到头部的列表值序列，例如[1,2,3]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is not None:
            temp = listNode
            lists = []
            while temp is not None:
                lists.insert(0, temp.val)
                temp = temp.next
            print lists