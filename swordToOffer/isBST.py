#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 递归版本1
        if not sequence:
            return False
        length = len(sequence)
        if length==1:
            return True
        root=sequence[-1]
        i=0
        # 后序遍历是： 左-右-根，最后一个是根元素，将前面的序列分成两部分：左子树和右子树
        while sequence[i]<root:
            i+=1
        j=i
        # 如果右子树中有元素小于根节点，返回False
        for m in range(j,length-1):
            if sequence[m]<root:
                return False
        left=True
        if len(sequence[:i])>0:
            left=self.VerifySquenceOfBST(sequence[:i])
        right=True
        if len(sequence[i:length-1])>0:
            right=self.VerifySquenceOfBST(sequence[i:length-1])
        return left and right

    def VerifySquenceOfBST1(self,sequence):
        # 递归版本2
        if not sequence:
            return False
        length=len(sequence)
        return self.judge(sequence,0,length-1)

    def judge(self,sequence,l,r):
        if l>=r:
            return True
        i=r
        while i>l and sequence[i-1]>sequence[r]:
            i-=1
        j=i-1
        while l<=j:
            if sequence[j]>sequence[r]:
                return False
            j-=1
        return self.judge(sequence,l,i-1) and self.judge(sequence,i,r-1)

    def VerifySquenceOfBST2(self,sequence):
        # 费递归版本
        if not sequence:
            return False
        i=0
        size=len(sequence)-1
        while size:
            while sequence[i]<sequence[size]:
                i+=1
            while sequence[i]>sequence[size]:
                i+=1
            if i<size:
                return False
            i=0
            size-=1
        return True



if __name__=="__main__":
    s=Solution()
    print s.VerifySquenceOfBST2([5,7,6,9,11,10,8])