#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""


class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    def FindPath(self, root, expectNumber):
        ans=[]
        temp=[]
        if root:
            self.dfsFind(root, expectNumber,ans,temp)
        return ans

    def dfsFind(self, root, expectNumber,ans,temp):
        temp.append(root.val)
        if expectNumber == root.val and (not root.left) and (not root.right):
            ans.append(temp)
        if root.left:
            self.dfsFind(root.left, expectNumber - root.val,ans,temp)
        if root.right:
            self.dfsFind(root.right, expectNumber - root.val,ans,temp)
        temp.pop()

if __name__ == "__main__":
    s = Solution()
    Tree = TreeNode(
        8, TreeNode(
            7, TreeNode(14), TreeNode(3)), TreeNode(
            6, right=TreeNode(1)))
    print s.FindPath(Tree, 15)
