#!/usr/bin/env python
# -*- coding: utf-8 -*-
#输入一个链表，输出该链表中倒数第k个结点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseLinkedList(self, pHead):
        if not pHead:
            return None
        reversedNode=None
        pre=None
        node=pHead
        while node!=None:
            pNext=node.next
            if pNext==None:
                reversedNode=node
            pre=node
            node=pNext
        return reversedNode




