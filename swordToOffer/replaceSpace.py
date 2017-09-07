#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer第二题
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replaceSpace(string):
    string=[j for j in string]
    spaceNum = string.count(' ')
    indexOld = len(string) - 1
    string += ' ' * 2 * spaceNum
    indexNew=len(string)-1
    for i in range(indexOld, -1, -1):
        if string[i] == ' ':
            string[indexNew] = '0'
            indexNew -= 1
            string[indexNew] = '2'
            indexNew -= 1
            string[indexNew] = '%'
            indexNew -= 1
        else:
            string[indexNew] = string[i]
            indexNew-=1
    return ''.join(string)

print replaceSpace(' h1')
