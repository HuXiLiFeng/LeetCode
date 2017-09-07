#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 快速排序
def part(lists,first,last):
    '''
    :param lists: 待排序列表
    :param first: 第一个索引值
    :param last: 最后一个索引值
    :return:
    '''
    pivot=lists[first]
    low=first+1
    high=last
    while high>low:
        while low<=high and lists[low]<=pivot:
            low+=1
        while low<=high and lists[high]>pivot:
            high-=1
        if high>low:
            lists[high],lists[low]=lists[low],lists[high]
    while high>first and lists[high]>=pivot:
        high-=1
    if pivot>lists[high]:
        lists[first]=lists[high]
        lists[high]=pivot
        return high
    else:
        return first

def quickSort(lists,first,last):
    if last>first:
        pivotIndex=part(lists,first,last)
        quickSort(lists,first,pivotIndex-1)
        quickSort(lists,pivotIndex+1,last)
    return lists


print quickSort([2,1,4,0,7,5],0,5)