#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
"""
def Fibonacci(n):
    if n<=0 or n>39:
        return 0
    elif n==1:
        return 1
    else:
        i=2
        first=0
        last=1
        while i<=n:
            temp=first+last
            first=last
            last=temp
            i+=1
        return last

def jump(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else: return  jump(n-1)+jump(n-2)
print jump(4)