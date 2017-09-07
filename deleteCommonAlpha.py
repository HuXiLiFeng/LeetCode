#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
"""


def help(n, m, lists, beg):
    if m == 0:
        for j in xrange(len(lists)):
            if j==0:
                print lists[j]
    i = beg
    while i <= n and i <= m:
        lists.append(i)
        help(n, m - i, lists, i + 1)
        lists.pop()
        i+=1
# temp = [int(i) for i in raw_input().split()]
n = 5
m = 5
lists = []
help(n, m, lists, 1)
