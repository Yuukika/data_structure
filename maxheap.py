#!/usr/bin/env python
# -*-coding:utf-8-*-



class MinHeap:
    """
    类型名称： 最小堆

    数据对象集：完全二叉树，每个结点的元素都不小于其子结点元素

    操作集：
    create , isfull, insert, inempty, deletemax
    """

    def __init__(self):
        self.size = 0
        self.data = [0]

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

        while self.data[i//2] > item:
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
        temp = self.data[-1]
        parent = 1
        while 2*parent <= self.size:
            child = parent * 2
            if child != self.size and self.data[child] > self.data[child+1]:
                child += 1
            if self.data[child] > temp:
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
        利用数组构建最小堆
        """
        self.data.extend(datalist)
        self.size = len(self.data) - 1
        i = (self.size + 1) // 2
        while i > 0:
            item = self.data[i]
            parent = i
            while 2*parent <= self.size:
                child = 2 * parent
                if child != self.size and self.data[child] > self.data[child+1]:
                    child += 1
                if item < self.data[child]:
                    break
                else:
                    self.data[parent] = self.data[child]
                parent = child
            self.data[parent] = item
            i -= 1

        return None




























