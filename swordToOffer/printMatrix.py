#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
顺时针打印矩阵
"""
matrix = [[1]]
row = len(matrix)
column = len(matrix[0])
k = 0
i = 0
j = 0
loop = (min(row, column) + 1) / 2
while k < loop:
    startRow = i + k
    endRow = row - k - 1
    startColumn = j + k
    endColumn = column - k - 1
    for c in range(startColumn, endColumn + 1):
        print matrix[startRow][c],
    for r in range(startRow + 1, endRow):
        print matrix[r][endColumn],
    if startRow != endRow:
        for c in range(endColumn, startColumn - 1, -1):
            print matrix[endRow][c],
        for r in range(endRow - 1, startRow, -1):
            print matrix[r][startColumn],
    k += 1
print "\n下面是剑指的方法：\r"

def printMatrixInCircle(matrix,row,column,start):
    endX=column-1-start
    endY=row-1-start
    """从左到右打印一行"""
    for i in xrange(start,endX+1):
        print matrix[start][i],
    """从上到下打印每列"""
    if endY>start:
        for i in xrange(start+1,endY+1):
            print matrix[i][endX],
    """从右到左打印每行"""
    if endX>start:
        for i in xrange(endX-1,start-1,-1):
            print matrix[endY][i],
    """从下到上打印每列"""
    if endY-1>start and start<endX:
        for i in xrange(endY-1,start,-1):
            print matrix[i][start],

def printMatrix(matrix):
    if not matrix:
        return None
    row=len(matrix)
    column=len(matrix[0])
    start=0
    while column>start*2 and row>start*2:
        printMatrixInCircle(matrix,row,column,start)
        start+=1

printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])