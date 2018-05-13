#!/usr/bin/env python
# -*-coding:utf-8-*-


# 二分查找

def binarysearch(tbl, k):
    left = 0
    right = len(tbl) - 1
    while left <= right:
        mid = (left + right) // 2
        if K < tbl[mid]:
            right = mid - 1
        elif K > tbl[mid]:
            left = mid + 1
        else:
            return mid
        return -1

"""
树的定义:
n个结点构成的有限集合
根节点：r
结点的度
树的度
叶结点
父结点
"""

"""
    二叉树的定义:
    斜二叉树
    完美二叉树
    完全二叉树

    抽象数据类型定义：

    类型名称：二叉树
    数据对象集：一个有穷的结点集合。
    若不为空，则由根节点和其左右二叉子书组成。
    三个重要操作：
        1、 判别BT是否为空
        2、 遍历， 按某顺序访问每个界定啊
        3、 创建一个二叉树

    常见的遍历方法：
        1、 先序--- 根、左子树、右子树
        2、 中序--- 左子树，根， 右子树
        3、 后序--- 左子树， 右子树， 根
        4、 层次遍历---，从上到下， 从左到右

    顺序存储结构的一些特点：
    1、 非根节点的结点i的父节点的序号是i//2
    2、 结点i的左子结点的序号是2i，在存在的情况下
    3、 结点i的右子结点的序号是2i+1，在存在的情况下
"""
class Tnode:
    def __init__(self,data):
        """
        采用链表构建的树的结点类
        """
        self.data = data
        self.left = None
        self.right = None
        #self.child_node = (self.left or self.right)
    def __repr__(self):
        return self.data

# 先序遍历树结点
def PreOrderTraversal(tree_node):
    """
    遍历过程：
    访问根结点
    先序遍历其左子树
    先序遍历其右子树
    """
    if tree_node:
        print('{0}'.format(tree_node.data))
        preOrderTraversal(tree_node.left)
        preOrderTraversal(tree_node.right)
# 中序遍历树结点
def InOrderTraversal(tree_node):
    """
    遍历过程为：
    中序遍历其左子树
    访问根结点
    中序遍历其右子树
    """
    if tree_node:
        InOrderTraversal(tree_node.left)
        print('{0}'.format(tree_node.data))
        InOrderTraversal(tree_node.right)

# 后序遍历
def PostOrderTraversal(tree_node):
    """
    遍历过程为：
    后序遍历其左子树
    后序遍历其右子树
    访问根结点
    """
    if tree_node:
        PostOrderTraversal(tree_node.left)
        PostOrderTraversal(tree_node.right)
        print('{0}'.format(tree_node.data))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
class Snode:
    """
    堆栈类
    包含push,pop,show_all(显示所有数据)方法
    """
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, node):
        if isinstance(node, Node):
            pass
        else:
            node = Node(node)

        if not self.head:
            self.head = node
        else:
            next_cell = self.head
            self.head = node
            self.head.next = next_cell
        self.length += 1
        return

    def pop(self):
        if self.is_empty():
            print('堆栈空')
            return
        else:
            node = self.head
            tnode = node.data
            self.head = self.head.next
            del node
            self.length -= 1
            return tnode

    def show_all(self):
        if self.is_empty():
            #print('堆栈为空')
            return
        else:
            node = self.head
            print(node.data.data, end=' ')
            while node.next:
                node = node.next
                print(node.data.data, end=' ')
            print('None')

# 不使用递归方法来是实现树的四种遍历
def InOrderTraversal2(tree_node):
    """
    利用堆栈来实现中序遍历:
    左，中，右

    """
    stack = Snode()
    while(tree_node or not stack.is_empty()):
        while tree_node:
            stack.push(tree_node)
            tree_node = tree_node.left
        if not stack.is_empty():
            tree_node = stack.pop()
            print('{0}'.format(tree_node.data))
            tree_node = tree_node.right


def PreOrderTraversal2(tree_node):
    """
    利用堆栈俩是实现先序遍历:
    中，左，右
    """
    stack = Snode()
    while tree_node or not stack.is_empty():
        while tree_node:
            print('{0}'.format(tree_node.data))
            stack.push(tree_node)
            tree_node = tree_node.left
        if not stack.is_empty():
            tree_node = stack.pop()
            tree_node = tree_node.right

def PostOrderTraversal2(tree_node):
    """
    利用堆栈俩是实现先序遍历:
    左，右，中


    未完成
    """
    stack = Snode()
    while tree_node or not stack.is_empty():
        while tree_node:
            stack.push(tree_node)
            if tree_node.right:
                stack.push(tree_node)
            tree_node = tree_node.left
        #print('{0}'.format(tree_node.data))
        if not stack.is_empty():
            tree_node = stack.pop()
            if tree_node.right:
                stack.push(tree_node)
                tree_node = tree_node.right

class Qnode:
    """
    采用链式存储实现队列
    """
    def __init__(self):
        self.length = 0
        self.rear = None
        self.front = None

    def isEmpty(self):
        return self.length == 0

    def addq(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.length == 0:
            self.rear = node
            self.front = node

        else:
            self.rear.next = node
        self.length += 1
        return
    def deleteq(self):
        if self.length == 0:
            print('空队列')
        datanode = self.front
        if self.front.next:
            self.front = self.front.next
        else:
            self.front = self.rear = None
        data = datanode.data
        del(datanode)
        self.length -= 1
        return data

    def show_all(self):
        node = self.front
        while node:
            print(node.data, '-->', end=' ')
            node = node.next
        print('None')

def LevelOrderTraversal(tree_node):
    if not tree_node:
        return
    queue = Qnode()
    queue.addq(tree_node)

    while not queue.isEmpty():
        tree_node = queue.deleteq()
        print('{0}'.format(tree_node.data))
        if tree_node.left:
            queue.addq(tree_node.left)
        if tree_node.right:
            queue.addq(tree_node.right)


if __name__ == '__main__':
    # 构造一个二叉树
    node_e = Tnode('E')
    node_h = Tnode('H')
    node_d = Tnode('D')
    node_i = Tnode('I')
    node_f = Tnode('F')
    node_f.left = node_e
    node_g = Tnode('G')
    node_g.right = node_h
    node_b = Tnode('B')
    node_b.left = node_d
    node_b.right = node_f
    node_c = Tnode('C')
    node_c.left = node_g
    node_c.right = node_i
    node_a = Tnode('A')
    node_a.left = node_b
    node_a.right = node_c
    #PreOrderTraversal2(node_a)
    #InOrderTraversal2(node_a)

    LevelOrderTraversal(node_a)