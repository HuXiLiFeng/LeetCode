#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


def NumberOf1( n):
    count=0
    while n:
        if n&1:
            count+=1
        n=n>>1
    return count

def numberof1(n):
    count=0
    while n:
        count+=1
        n=n&(n-1)
    return count

print numberof1(12)