#!/usr/bin/env python
# -*-coding:utf-8-*-

class Qnode:
    """
    队列：具有一定操作约束的线性表
    插入和删除操作：只能在一段插入，而在另一端删除

    输入插入：入队列
    数据删除： 出队列

    先来先服务
    先进先出

    操作集:
    createqueue

    isempty

    addq

    deleteq
    """
    def __init__(self, maxsize):
        self.data = []
        self.length = 0
        self.maxsize = maxsize
        self.rear = 0
        self.front = 0


    def full_list(self):
        return self.length == self.maxsize

    def addq(self, value):
        if self.rear%self.maxsize == self.front and self.full_list():
            print('队列满了')
            return

        else:
            try:
                self.data[self.rear] = value
            except:
                self.data.append(value)
            self.rear = (self.rear+1)% self.maxsize
            self.length += 1
    def deleteq(self):
        if self.rear == self.front and not self.full_list():
            print('队列为空')
            return None
        else:
            value = self.data[self.front]
            self.front = (self.front+1)% self.maxsize
            self.length -= 1
            return value
    def show_all_list(self):
        if  self.full_list():
            if self.rear > self.front:
                for i in range(self.front, self.rear):
                    print(self.data[i], end=' ')
            else:
                for i in range(self.front, self.rear+self.maxsize):
                    print(self.data[i%self.maxsize], end=' ')
        else:
            print('队列为空')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Qnode2:
    """
    采用链式存储实现
    """
    def __init__(self):
        self.length = 0
        self.rear = None
        self.front = None

    def addq(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.length == 0:
            self.rear = node
            self.front = node

        else:
            self.rear.next = node
            self.rear = self.rear.next
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





if __name__ == '__main__':

    qnode = Qnode2()
    qnode.addq('I')
    qnode.addq('Like')
    qnode.addq('you')
    qnode.addq('very')
    qnode.deleteq()
    qnode.deleteq()
    #qnode.deleteq()
    qnode.addq('do')
    qnode.show_all()