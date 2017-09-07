#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定单向链表的头结点和其中的一个节点，要求以O(1)时间删除该节点
"""
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def createList(n):
    if n<=0:
        return
    if n==1:
        return Node(1)
    else:
        head=Node(1)
        temp=head
        for i in range(2,n+1):
            temp.next=Node(i)
            temp=temp.next
    return head

def delNode(LinkedList,node):
    if not LinkedList and not node:
        return None
    if node.next:
        # 要删除的不是尾节点
        pNext=node.next
        node.val=pNext.val
        node.next=pNext.next
    elif LinkedList==node:
        #链表只有一个节点，删除该节点
        LinkedList=None
        node=None
    else:
        #删除尾节点
        while LinkedList.next!=node:
            LinkedList=LinkedList.next
        LinkedList.next=None
        node=None

if __name__=="__main__":
    node=createList(5)
    delNode(node,Node(5))
