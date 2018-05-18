#!/usr/bin/env python
# -*-coding:utf-8-*-

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,maxsize):
        self.treelist = [-1 for i in range(maxsize)]


def buildtree():
    maxsize = eval(input("请输入结点数:"))
    tree = Tree(maxsize)
    if maxsize:
        for i in range(maxsize):
            data,left,right= eval(input("依次输入每个结点的数据，左子结点和右子结点:"))
            tree.treelist[i] = TreeNode(data)
            if left != '-':
                tree.treelist[i].left = left
            if right != '-':
                tree.treelist[i].right = right
    return tree


def isomorphic(t1, t2):



if __name__ == '__main__':
    tree1 = buildtree()
