#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

class Solution:
    def reOrderArray(self, array):
        if not array:
            return None
        length=len(array)
        i=0
        j=length-1
        while i<j:
            while i<j and array[i]&0x1==1:
                i+=1
            while i<j and array[j]&0x1==0:
                j-=1
            if i<j:
                array[i],array[j]=array[j],array[i]
        return array

    def reOrder(self,array):
        length=len(array)
        i=length-1
        while i>0:
            if i==1:
                if array[0]&0x1==1:
                    return array
                else:
                    key=array[0]
                    while array[i]&0x1==1:
                        array[i]=array[i+1]
                        i+=1
                    array[i-1]=key
            while i>0 and array[i]&0x1==0:
                i-=1
            j=i-1
            while j>=0 and array[j]&0x1==1:
                j-=1
            if j==-1:
                return array
            key=array[j]
            for item in xrange(j,i):
                array[item]=array[item+1]
            array[i]=key
            i-=1
        return array
if __name__=="__main__":
    s=Solution()
    print s.reOrderArray([1,2,3,4,5,6,7,8,9])
    print s.reOrder([1,2,3,4,5,6,7])