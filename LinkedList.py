#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
实现链表相关功能
"""


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        temp = l1
        while temp is not None:
            a.insert(0, temp.val)
            temp = temp.next
        t1 = ''
        for i in a:
            t1 += str(i)
        b = []
        temp1 = l2
        while temp1 is not None:
            b.insert(0, temp1.val)
            temp1 = temp1.next
        t2 = ''
        for i in b:
            t2 += str(i)
        result = int(t1) + int(t2)
        result = str(result)[::-1]
        l3 = [int(i) for i in str(result)]
        re = Node(l3[0])
        temp2 = re
        for i in range(1, len(l3)):
            temp2.next = Node(l3[i])
            temp2 = temp2.next
        return re

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1, x2 = 0, 0
        while l1:
            x1 = x1 * 10 + l1.val
            l1 = l1.next
        while l2:
            x2 = x2 * 10 + l2.val
            l2 = l2.next
        x = x1 + x2
        result = str(x)
        temp3 = Node(result[0])
        temp4 = temp3
        for i in range(1, len(result)):
            temp4.next = Node(int(result[i]))
            temp4 = temp4.next
        return temp3


class Node():

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def createList(n):
    if n <= 0:
        return
    if n == 1:
        return Node(1)
    else:
        head = Node(1)
        temp = head
        for i in range(2, n + 1):
            temp.next = Node(i)
            temp = temp.next
    return head


def printList(head):
    p = head
    while p is not None:  # 这里是判断下一个对象是否为None
        print p.val
        p = p.next


def listLength(head):
    p = head
    length = 0
    while p is not None:  # 这里是判断下一个对象是否为None
        length += 1
        p = p.next
    return length


def insert(head, idx, val):
    if idx < 0 or idx > listLength(head):
        return
    elif idx == 1:
        temp = Node(val, head)
        return temp
    else:
        p = head
        length = 1
        while length < idx - 1:
            length += 1
            p = p.next

        t = Node(val)
        t.next = p.next
        p.next = t
        return head


def delete(head, idx):
    if idx < 0 or idx > listLength(head):
        return
    elif idx == 1:
        return head.next
    else:
        p = head
        length = 1
        while length < idx - 1:
            length += 1
            p = p.next
        temp = p.next
        p.next = temp.next

        return head


def createListNode(lists):
    head = Node(lists[0])
    temp = head
    if len(lists) > 1:
        for i in range(1, len(lists)):
            temp.next = Node(lists[i])
            temp = temp.next
    return head


def reversedLinkedList(pHead):
    # 循环大法，反转链表
    pPre = None
    cur = pHead
    reversedHead = None
    while cur:
        pNext = cur.next
        if pNext is None:
            reversedHead = cur
        cur.next = pPre
        pPre = cur
        cur = pNext
    return reversedHead


def reveredLinkedList1(pHead):
    # 递归方法逆转链表
    if not pHead or not pHead.next:
        return pHead
    pNewHead = reveredLinkedList1(pHead.next)
    pHead.next.next = pHead
    pHead.next = None
    return pNewHead


def reveredLinkedList2(pHead):
    # 遍历逆转链表
    if pHead is None or pHead.next is None:
        return pHead
    reversed = None
    current = pHead
    while current is not None:
        temp = current
        current = current.next
        temp.next = reversed
        reversed = temp
    return reversed

def findItem(pHead,k):
    """
    查找倒数第k个节点
    :param pHead:
    :param k:
    :return:
    """
    if k==0 or pHead is None:
        return None
    first=pHead
    while k>1 and pHead is not None:
        pHead=pHead.next
        k-=1
    if k>1 or pHead is None:
        return None
    while pHead.next is not None:
        pHead=pHead.next
        first=first.next
    return first

def findMidItem(pHead):
    """
    寻找链表中间的节点
    :param pHead:
    :return:
    """
    if pHead is None or pHead.next is None:
        return pHead
    first=pHead
    while pHead.next is not None:
        if pHead.next.next is None:
            pHead=pHead.next
        else:
            pHead=pHead.next.next
        first = first.next
    return first


def reversedPrint(pHead):
    """
    逆序打印链表,利用栈，遍历一个存一个，然后输出
    :param pHead:
    :return:
    """
    if pHead is None:
        return None
    lists=[]
    while pHead is not None:
        lists.append(pHead.val)
        pHead=pHead.next
    print lists[::-1]

def recursivePrint(pHead):
    """
    递归逆序打印链表
    :param pHead:
    :return:
    """
    if pHead.next==None:
        print pHead.val
    if pHead is not None:
        recursivePrint(pHead.next)
    print pHead.val

def merge(pHead1,pHead2):
    """
    合并两个有序的链表，将pHead2链表插入到pHead1中
    :param pHead1:
    :param pHead2:
    :return:
    """
    if pHead1 is None:
        return pHead2
    if pHead2 is None:
        return pHead1
    if pHead1.val<pHead2.val:
        pHeadMerged=pHead1
        pHead1=pHead1.next
    else:
        pHeadMerged=pHead2
        pHead2=pHead2.next
    pTemp=pHeadMerged
    while pHead1 is not None and pHead2 is not None:
        if pHead1.val<pHead2.val:
            pTemp.next=pHead1
            pHead1=pHead1.next
            pTemp=pTemp.next
        else:
            pTemp.next=pHead2
            pHead2=pHead2.next
            pTemp=pTemp.next
    if pHead2:
        pTemp.next=pHead2
    elif pHead1:
        pTemp.next=pHead1
    return pHeadMerged

def mergeRecursive(pHead1,pHead2):
    """
    递归方法合并两个有序链表
    :param pHead1:
    :param pHead2:
    :return:
    """
    if pHead1 is None:
        return pHead2
    if pHead2 is None:
        return pHead1
    if pHead1.val<pHead2.val:
        pHeadMerged=pHead1
        pHeadMerged.next=mergeRecursive(pHead1.next,pHead2)
    else:
        pHeadMerged=pHead2
        pHeadMerged.next=mergeRecursive(pHead1,pHead2.next)
    return pHeadMerged

def isLoop(pHead1):
    """
    判断一个链表中是否有环
    :param pHead1:
    :return:
    """
    pSlow=pHead1
    pFast=pHead1
    while pFast is not None and pFast.next is not None:
        pSlow=pSlow.next
        pFast=pFast.next.next
        if pFast==pSlow:
            return True
    return False

def IsIntersected(pHead1,pHead2):
    """
    判断两个链表是否相交
    :param pHead1:
    :param pHead2:
    :return:
    """
    if pHead1 is None or pHead2 is None:
        return None
    while pHead1.next is not None:
        pHead1=pHead1.next
    while pHead2.next is not None:
        pHead2=pHead2.next
    if pHead1==pHead2:
        return True
    else:
        return False

def getFirstCommonNode(pHead1,pHead2):
    """
    两个链表的交点
    :param pHead1:
    :param pHead2:
    :return:
    """
    if pHead1 is None or pHead2 is None:
        return None
    len1=1
    len2=1
    p1=pHead1
    p2=pHead2
    while p1:
        len1 += 1
        p1=p1.next
    while p2:
        len2+=1
        p2=p2.next
    if len1>len2:
        diff=len1-len2
        while diff>0:
            pHead1=pHead1.next
            diff-=1
    else:
        diff=len2-len1
        while diff>0:
            pHead2=pHead2.next
            diff-=1
    while pHead1.val != pHead2.val:
        pHead1=pHead1.next
        pHead2=pHead2.next
    return pHead1.val


def findCircleNode(pHead1):
    """
    查找环的入口节点
    :param pHead1:
    :return:
    """
    pSlow = pHead1
    pFast = pHead1
    temp=None
    while pFast is not None and pFast.next is not None:
        pSlow = pSlow.next
        pFast = pFast.next.next
        if pFast == pSlow:
            temp=pSlow
    while pHead1!=temp:
        pHead1=pHead1.next
        temp=temp.next
    return pHead1



if __name__ == "__main__":
    # a=createList(5)
    # printList(a)
    # print "创建链表长度为：%s"%listLength(a)
    # print "=="*4
    # b=insert(a,5,0)
    # printList(b)
    # print "=="*4
    # c=delete(b,3)
    # printList(c)
    a = createListNode([2,6,9,11,24])
    b=createListNode([1,3,10,9,11,24])
    # rever = findMidItem(a)
    # print rever.val
    # reversedPrint(a)
    # cur=mergeRecursive(a,b)
    # print cur.val
    # print isLoop(a)
    print getFirstCommonNode(a,b)
    print findCircleNode(b)

