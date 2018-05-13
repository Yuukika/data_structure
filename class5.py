#!/usr/bin/env python
# -*-coding:utf-8-*-

import time

"""
堆就是有优先级的队列，取出元素按照元素的优先权大小，而不是元素进入队列的先后顺序

结构性：用数组表示完全二叉树

有序性： 任一结点的关键字是其子树所有结点的最大值或者最小值
1、MaxHeap 大顶堆
2、MinHeap 小顶堆

"""

class MaxHeap:
    """
    类型名称： 最大堆

    数据对象集： 完全二叉树，每个结点的元素都不小于其子结点元素

    操作集：
    create , isfull, insert, isempty, deletemax
    """
    def __init__(self):
        """
        初始化最大堆
        """
        self.size = 0
        self.data = [1000]
    def is_empty(self):
        """
        判定最大堆是否为空
        """
        return self.size == 0
    def insert(self, item):
        """
        向堆中插入数据
        """
        self.data.append(item)
        self.size += 1
        i = self.size

        while self.data[i//2] < item:
            self.data[i] = self.data[i//2]
            i //= 2
        self.data[i] = item
        return

    def delete(self):
        """
        从最大堆中推出最大值
        """
        if self.is_empty():
            print('最大堆已经为空')
            return None
        item = self.data[1]
        temp = self.data[-1]
        parent = 1
        while 2*parent <= self.size:
            child = parent * 2
            if child != self.size and self.data[child] < self.data[child + 1]:
                child += 1
            if self.data[child] < temp:
                break
            else:
                self.data[parent] = self.data[child]
            parent = child
        self.data[parent] = temp
        self.size -= 1
        return item

    def show_all(self):
        print(self.data[1:self.size+1])
    def buildheap(self, datalist):
        """
        利用数组构建最大堆
        """
        self.data.extend(datalist)
        self.size = len(self.data) - 1
        i = (self.size + 1) // 2
        while i > 0:
            item = self.data[i]
            parent = i
            while 2*parent <= self.size:
                child = 2 * parent
                if child != self.size and self.data[child] < self.data[child+1]:
                    child += 1
                if item > self.data[child]:
                    break
                else:
                    self.data[parent] = self.data[child]
                parent = child
            self.data[parent] = item
            i -= 1

        return None



class MinHeap:
    """
    类型名称： 最小堆

    数据对象集：完全二叉树，每个结点的元素都不小于其子结点元素

    操作集：
    create , isfull, insert, inempty, deletemax
    """

    def __init__(self):
        self.size = 0
        self.data = [TreeNode(0)]

    def is_empty(self):
        """
        判定最大堆是否为空
        """
        return self.size == 0

    def insert(self, item):
        """
        向堆中插入数据
        """
        if not isinstance(item, TreeNode):
            item = TreeNode(item)
        else:
            pass
        self.data.append(item)
        self.size += 1
        i = self.size

        while self.data[i//2].weight > item.weight:
            self.data[i] = self.data[i//2]
            i //= 2
        self.data[i] = item
        return

    def delete(self):
        """
        向堆中插入数据
        """

        if self.is_empty():
            print('最小堆已经为空')
            return None
        item = self.data[1]
        temp = self.data[self.size]
        parent = 1
        while 2*parent <= self.size:
            child = parent * 2
            if child != self.size and self.data[child].weight > self.data[child+1].weight:
                child += 1
            if self.data[child].weight > temp.weight:
                break
            else:
                self.data[parent] = self.data[child]
            parent = child
        self.data[parent] = temp
        self.size -= 1
        #print('temp=', temp.weight)

        return item

    def show_all(self):
        if not self.is_empty():
            weight_list = []
            for i in range(1,self.size+1):
                weight_list.append(self.data[i].weight)
            print(weight_list)

    def buildheap(self, datalist):
        """
        利用数组构建最小堆
        """
        for i in range(0,len(datalist)):
            if not isinstance(datalist[i], TreeNode):
                datalist[i] = TreeNode(datalist[i])
            else:
                pass
        self.data.extend(datalist)
        self.size = len(self.data) - 1
        i = (self.size + 1) // 2
        while i > 0:
            item = self.data[i]
            parent = i
            while 2*parent <= self.size:
                child = 2 * parent
                if child != self.size and self.data[child].weight > self.data[child+1].weight:
                    child += 1
                if item.weight < self.data[child].weight:
                    break
                else:
                    self.data[parent] = self.data[child]
                parent = child
            self.data[parent] = item
            i -= 1

        return None

"""
Huffman Tree

带权路径长度（WPL）：设二叉树有n个叶子结点，每个叶子结点带有权值wk,从根节点到每个叶子结点的长度为lk,
则每个叶子结点的带权路径长度之和就是WPL: sum(wk*lk)(k=1...n)

WPL最小的二叉树就称为最优二叉树或者哈弗曼树


二叉树有n个叶子结点，每个叶子结点带有权值wk,
构造哈夫曼树： 每次把权值最小的两棵二叉树合并
"""
class TreeNode:
    def __init__(self,weight):
        self.weight = weight
        self.left = self.right = None

def huffman(minheap):
    """
    二叉树有n个叶子结点，每个叶子结点带有权值wk,
    构造哈夫曼树： 每次把权值最小的两棵二叉树合并
    哈夫曼树的特点：
    1、没有度为1的结点
    2、n个结点的哈夫曼树共有2n-1个结点
    3、哈夫曼树的任意非叶节点的左右子树交换后仍旧是哈夫曼树
    4、对于一组权值，存在不同构的哈夫曼树
    """
    for i in range(1,minheap.size):
        tree_node= TreeNode(0)
        tree_node.left = minheap.delete()
        tree_node.right = minheap.delete()
        tree_node.weight = tree_node.left.weight + tree_node.right.weight
        minheap.insert(tree_node)

    return minheap.delete()

def PreOrderTraversal(tree_node):
    """
    遍历过程：
    访问根结点
    先序遍历其左子树
    先序遍历其右子树
    """
    if tree_node:
        print(tree_node.weight,end=' ')
        PreOrderTraversal(tree_node.left)
        PreOrderTraversal(tree_node.right)




if __name__ == '__main__':
    minheap = MinHeap()
    #minheap.insert(12)
    #minheap.insert(9)
    #minheap.insert(14)
    #minheap.insert(7)
    #minheap.show_all()
    #minheap.delete()
    minheap.buildheap([1,3,2,4,5,6])
    tree_node = huffman(minheap)



