#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
# 二叉数搜索
1、非空左子树的所有键值小于其根结点的键值
2、非空右子树的所有键值大于其根节点的键值
3、左、右子树都是二叉搜索树

find 从二叉搜索树中查找元素X, 返回其所在结点的地址

findmin 从二叉搜索树中查找并返回最小元素所在结点的地址

findmax 从二叉搜索树中查找并返回最大元素所在结点的地址

insert and delete
"""

class Tnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def createTree():
    """
    非空左子树的所有键值要小于根节点的键值
    非空右子树的所有键值要大于根节点的键值
    """
    h = Tnode(1)
    i = Tnode(7)
    j = Tnode(12)
    k = Tnode(17)
    d = Tnode(5)
    d.left = h
    d.right = i
    e = Tnode(15)
    e.left = j
    e.right = k
    f = Tnode(25)
    g = Tnode(35)
    b = Tnode(10)
    b.left = d
    b.right = e
    c = Tnode(30)
    c.left = f
    c.right = g
    a = Tnode(20)
    a.left = b
    a.right = c
    return a

def printf(tree_node):
    if tree_node:
        print('{0}'.format(tree_node.data))
        printf(tree_node.left)
        printf(tree_node.right)


def IterFind(tree_node, k):
    while tree_node:
        if k > tree_node.data:
            tree_node = tree_node.right
        elif k < tree_node.data:
            tree_node = tree_node.left
        else:
            return tree_node
    return None

def find_min(tree_node):
    if tree_node == None:
        return None
    else:
        while tree_node.left:
            tree_node = tree_node.left
        return tree_node

def find_max(tree_node):
    if tree_node == None:
        return None
    else:
        while tree_node.right:
            tree_node = tree_node.right
        return tree_node


def insert(k, tree_node):
    if not tree_node:
        tree_node = Tnode(k)
    else:
        if k < tree_node.data:
            tree_node.left = insert(k ,tree_node.left)
        else:
            tree_node.right = insert(k , tree_node.right)
    return tree_node

def delete(k, tree_node):
    if not tree_node:
        print('要删除的元素未找到')
    elif k > tree_node.data:
        tree_node.right = delete(k, tree_node.right)
    elif k < tree_node.data:
        tree_node.left = delete(k, tree_node.left)
    else:
        if tree_node.left and tree_node.right:
            tmp = find_min(tree_node.right)
            tree_node.data = tmp.data
            tree_node.right = delete(tmp.data, tree_node.right)
        else:
            tmp = tree_node
            if not tree_node.left:
                tree_node = tree_node.right
            elif not tree_node.right:
                tree_node = tree_node.left
            del tmp
    return tree_node
"""
### 平衡二叉树
balance factor BF = Hl - Hr
左右数的高度
balanced binary tree avl树
空树，或者左右子树高度差的绝对值不超过1

高度为h的avl数的最少节点数为nh = nh-1 + nh-2 + 1

给定结点数为n的avl数的最大高度为O(log2(n))

平衡二叉树的调整：
导致不平衡的结点在不平衡根结点右子树的右边：采用右单旋（RR旋转）
导致不平衡的结点在不平衡根结点左子树的左边：采用左单旋（LL旋转）

导致不平衡的结点在不平衡根结点左子树的右边：采用LR旋转

导致不平衡的结点在不平衡根结点右子树的左边：采用RL旋转


"""


if __name__ == '__main__':
    tnode = createTree()
    printf(tnode)
    #printf(IterFind(tnode,15))
    #printf(find_min(tnode))
    #printf(find_max(tnode))
    print('----------')
    #insert(21,tnode)
    delete(30, tnode)
    printf(tnode)