#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
返回构造的TreeNode根节点
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            rootIndex = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1 + rootIndex], tin[0:rootIndex])
            root.right = self.reConstructBinaryTree(pre[1 + rootIndex:], tin[rootIndex + 1:])
            return root


    def levelTravel(self,root):
        # 返回层次遍历
        if root is None:
            return
        result = [root]
        while len(result) !=0:
            t = result.pop(0)
            print t.val,
            if t.left is not None:
                result.append(t.left)
            if t.right is not None:
                result.append(t.right)


if __name__ == "__main__":
    pre = [1, 2, 3, 4, 5, 6, 7]
    tin = [3, 2, 4, 1, 6, 5, 7]
    s=Solution()
    root = s.reConstructBinaryTree(pre, tin)
    s.levelTravel(root)
