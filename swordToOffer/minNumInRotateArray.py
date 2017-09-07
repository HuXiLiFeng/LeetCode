#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""

class Solution:
    def minNumber(self, rotateArray):
        if not rotateArray:
            return None
        elif len(rotateArray)==1:
            return rotateArray[0]
        else:
            i=0
            while rotateArray[i]<rotateArray[i+1]:
                i+=1
            return rotateArray[i+1]

    def binarySearch(self,array):
        """
        二分查找可以将时间复杂度缩减到log(n)
        :param array:
        :return:
        """
        if not array:
            return None
        elif len(array)==1:
            return array[0]
        else:
            size = len(array)
            i=0
            j=size-1
            if array[i]<array[j]:
                return array[i]
            while j-i!=1:
                mid = (i + j) / 2
                if array[mid]==array[j] and array[i]==array[j]:
                    return min(array[i:j+1])

                if array[mid]>=array[i]:
                    i=mid
                else:
                    j=mid
            return array[j]


if __name__=="__main__":
    s=Solution()
    print s.minNumber([2,3,4,6,2,2,2])
    print s.binarySearch([1,0,1,1,1])