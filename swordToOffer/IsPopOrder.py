#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但
4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV and not popV:
            return False
        stack=[]
        # 用于标识弹出序列的位置
        popIndex=0
        for i in range(0,len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1]==popV[popIndex]:
                stack.pop()
                popIndex+=1
        # 辅助栈为空，该弹出序列是原序列出栈结果
        return True if not stack else False

if __name__=="__main__":
    s=Solution()
    print s.IsPopOrder([1,2,3,4,5],[4,5,3,2,1])