#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。复杂度为O(1)
"""

class Solution:
    def __init__(self,lists):
        self.lists=lists
        self.help=[]
    def push(self, node):
        self.lists.append(node)
        if not self.help or node<self.lists[-1]:
            self.help.append(node)
        if node>self.lists[-1]:
            self.help.append(self.help[-1])
    def pop(self):
        if len(self.help)>0 and len(self.lists)>0:
            self.help.pop()
            self.lists.pop()
    def min(self):
        if self.help:
            return self.help[-1]
        else:
            return None