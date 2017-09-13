#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
归并排序
"""

def sortArr(arr):
    if arr is None or len(arr)==1:
        return arr
    left=arr[:len(arr)/2]
    right=arr[len(arr)/2:]
    return merge(sortArr(left),sortArr(right))

def merge(left,right):
    # 将两个有序的序列合并
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        # 谁小就先存谁
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

print sortArr([1,2])