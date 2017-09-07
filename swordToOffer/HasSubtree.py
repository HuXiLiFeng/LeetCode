#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断pRoot2是否是pRoot1的子结构
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result=self.cmpTree(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def cmpTree(self,Tree1,Tree2):
        """Tree2 为空，说明Tree2遍历完了，即匹配成功"""
        if not Tree2:
            return True
        # Tree1为空，Tree2不为空，
        if not Tree1:
            return False
        if Tree1.val!=Tree2.val:
            return False
        return self.cmpTree(Tree1.left,Tree2.left) and self.cmpTree(Tree1.right,Tree2.right)