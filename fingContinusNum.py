#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
# 找出最长的连续数字串
def findContinusNum():
    lists=raw_input()
    temp=[]
    for i in range(len(lists)):
        if not lists[i].isdigit():
            temp.append(i)
    length=[]
    for i in range(len(temp)-1):
        length.append(temp[i+1]-temp[i]-1)
    if temp[-1]<len(lists)-1:
        length.append(len(lists)-1-temp[-1])
    idx=length.index(max(length))
    print lists[temp[idx]+1:temp[idx]+1+max(length)]

def findContinusNum1():
    #一种用正则表达式匹配的方法，寻找输入的一串字符中最长的连续数字
    input_val = raw_input()
    split_char = re.split(r'\D*', input_val)
    print max(split_char, key=len)

findContinusNum1()
