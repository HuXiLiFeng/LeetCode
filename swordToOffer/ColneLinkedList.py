#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x,next=None,random=None):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def CloneNodes(self, pHead):
        # 在原始链表的每个节点后面插入一个复制节点
        pRoot=pHead
        while pRoot:
            pClone=RandomListNode(pRoot.label)
            pClone.next=pRoot.next
            pRoot.next=pClone
            pRoot=pClone.next

    def randomNode(self,pHead):
        # 将原始链表中每个节点的random指示，赋给复制节点
        pNode=pHead
        while pNode:
            pClone=pNode.next
            if pNode.random:
                pClone.random=pNode.random.next
            pNode=pClone.next

    def pick(self,pHead):
        # 将复制节点挑出来，组成新链表
        pNode=pHead
        pClonedHead=None
        pCloned=None
        if pNode:
            pClonedHead=pCloned=pNode.next
            pNode.next=pCloned.next
            pNode=pNode.next
        while pNode:
            pCloned.next=pNode.next
            pCloned=pCloned.next
            pNode=pCloned.next
        return pClonedHead

    def Clone(self,pHead):
        self.Clone(pHead)
        self.randomNode(pHead)
        return self.pick(pHead)
