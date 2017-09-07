#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    if root is None:
        return
    print root.value,
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    if root is None:
        return
    midTraverse(root.left)
    print root.value,
    midTraverse(root.right)


def afterTraverse(root):
    if root is None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print root.value,


def levelTraverse(root):
    """
    层次遍历
    :param root:
    :return:
    """
    if root is None:
        return None
    q = [root]
    while q:
        current = q.pop(0)
        print current.value,
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)


def depthFirstTravel(root):
    """
    深度遍历
    :param root:
    :return:
    """
    stack=[]
    stack.append(root)
    while stack:
        root=stack.pop()
        print root.value,
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)



def preOrder(root):
    """
    非递归输出前序遍历
    :param root:
    :return:
    """
    if root is None:
        return
    q = []
    pNode = root
    while pNode is not None or q:
        if pNode is not None:
            print pNode.value,
            q.append(pNode)
            pNode = pNode.left
        else:
            node = q.pop(-1)
            pNode = node.right


def preOrder1(root):
    """
    非递归方式实现的前序遍历
    :param root:
    :return:
    """
    if not root:
        return
    stackNode = [root]
    while stackNode:
        node = stackNode.pop()
        print node.value,
        if node.right:
            stackNode.append(node.right)
        if node.left:
            stackNode.append(node.left)


def inOrder(root):
    """
    非递归方式中序遍历
    :param root:
    :return:
    """
    if root is None:
        return
    q = []
    pNode = root
    while pNode is not None or q:
        if pNode is not None:
            q.append(pNode)
            pNode = pNode.left
        else:
            node = q.pop()
            print node.value,
            pNode = node.right


def inOrder1(root):
    """
    非递归方式实现中序遍历
    :param root:
    :return:
    """
    if not root:
        return
    stackNode = []
    node=root
    while stackNode or node:
        while node:
            stackNode.append(node)
            node=node.left
        node = stackNode.pop()
        print node.value,
        node=node.right


def postOrder(root):
    if not root:
        return
    stackNode = []
    markNode = None
    node = root
    while stackNode or node:
        while node:
            stackNode.append(node)
            node = node.left
        node = stackNode.pop()
        if not node.right or node.right is markNode:
            # node  has no rightNode or node's rightNode has been checked
            print node.value,
            markNode = node
            node = None
        else:
            stackNode.append(node)
            node = node.right


def findPostOrder(preList, midList, afterList):
    """
    给定前序和中序，求后序遍历
    :param preList:
    :param midList:
    :param afterList:
    :return:
    """
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findPostOrder(preList[1:n + 1], midList[:n], afterList)
    findPostOrder(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)


def getNodeNumberKthLevel(root,k):
    """
    第K层节点的个数
    :param root:
    :param k:
    :return:
    """
    if root is None or k<0:
        return 0
    if k==1:
        return 1
    numLeft=getNodeNumberKthLevel(root.left,k-1)
    numRight=getNodeNumberKthLevel(root.right,k-1)
    return numLeft+numRight


def getLeafNodeNum(root):
    """
    获取叶子节点个数
    :param root:
    :return:
    """
    if root is None:
        return 0
    if root.left==None and root.right==None:
        return 1
    numLeft=getLeafNodeNum(root.left)
    numRight=getLeafNodeNum(root.right)
    return numLeft+numRight

if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
   #         D
   #     B        E
   # A      C         G
   #                      F
    print('前序遍历：')
    preTraverse(root)
    print "\n"
    print('非递归前序遍历：')
    preOrder1(root)
    print "\n"
    print('中序遍历：')
    midTraverse(root)
    print "\n"
    print('非递归中序遍历：')
    inOrder1(root)
    print "\n"
    print('后序遍历：')
    afterTraverse(root)
    print "\n"
    print('非递归后序遍历：')
    postOrder(root)
    print "\n"
    print('层次遍历：')
    levelTraverse(root)
    print "\n"
    print "深度遍历"
    depthFirstTravel(root)
    print "\n"
    print "=="*20
    print "根据前序和中序生成后序遍历："
    preList = list('DBACEGF')
    midList = list('ABCDEFG')
    print "前序：",preList
    print "中序: ",midList
    afterList = []
    findPostOrder(preList,midList,afterList)
    print afterList
    print "=="*20
    print "第3层的节点数：%d" % getNodeNumberKthLevel(root,3)
    print "叶子节点个数：%d"%getLeafNodeNum(root)
