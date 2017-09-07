#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer第一题
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
从右上角,左下角开始找
"""


def finder1(array, target):
    """
    从左下角开始找
    :param array: 嵌套list形成array
    :param target: 待查找元素
    :return:
    """
    row = len(array) - 1
    j = 0
    while row >= 0 and j <= len(array[0]) - 1:
        if array[row][j] == target:
            return True
        elif array[row][j] > target:
            row -= 1
        else:
            j += 1
    return False

testArray = [[2, 3, 5], [8, 10, 16], [17, 19, 21], [25, 40, 100]]
# lists=np.array(testArray)
# print finder(lists, 1)
print finder1([[]], 11)
