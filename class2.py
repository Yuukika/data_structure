#!/usr/bin/env python
# -*-coding:utf-8-*-
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Mnode:
    def __init__(self,data):
        self.data = data
        self.sublist = None
        self.next = None
    def __repr__(self):
        return self.data

class MatrixNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def append(self, node):
        if isinstance(node, Node):
            pass
        else:
            node = Node(node)
        if self.is_empty():
            self.head = node
        else:
            this_node = self.head
            while this_node.next:
                this_node = this_node.next
            this_node.next = node
        self.length += 1
        return

    def insert(self, value, index):
        if type(index) is int:
            if index < 0 or index > self.length:
                print('Index is out of range')
                return
            else:
                node = Node(value)
                node_guide = self.head

                if index == 0:
                    self.head = node
                    node.next = node_guide
                    return
                while index - 1:
                    node_guide = node_guide.next
                    index -= 1
                node.next = node_guide.next
                node_guide.next = node
                self.length += 1
                return
        else:
            print('Index value is not int')
            return
    def delete(self, index):
        if type(index) is int:
            if index > self.length:
                print('index is out of range')
                return
            else:
                if index == 0:
                    self.head = self.head.next

                else:
                    node_guide = self.head
                    while index - 1:
                        node_guide = node_guide.next
                        index -= 1

                    node_guide.next = node_guide.next.next
                    self.length -= 1
                    return
        else:
            print('index value is not int.')
            return

    def update(self, value, index):

        if type(index) is int:
            if index > self.length:
                print('index value is out of range')
                return
            else:
                #node = Node(value)
                if index == 0:
                    self.head.data = value

                else:
                    node_guide = self.head
                    while index - 1:
                        node_guide  = node_guide.next
                        index -= 1

                    node_guide.next.data = value
                    return
        else:
            print('index value is not int')
            return

    def get_value(self, index):
        if type(index) is int:
            if index > self.length:
                print('index is out of range')
                return
            else:
                if index == 0:
                    return self.head.data
                else:
                    node_guide = self.head
                    while index - 1:
                        node_guide = node_guide.next
                        index -= 1
                    return node_guide.next.data
        else:
            print('index value is not int')
            return

    def get_length(self):
        node_guide = self.head
        if node_guide:
            i  = 1
            while node_guide.next:
                node_guide = node_guide.next
                i += 1
            return i
        else:
            return 0

    def clear(self):
        self.head = None
        self.length = 0
        print('Clear the linked list finished')


    def print_linked_list(self):
        if self.is_empty():
            print('linked list is empty')
        else:
            node = self.head
            print('Head -->', node.data, end = ' ')
            while node.next:
                node = node.next
                print('-->', node.data, end=' ')
            print('--> None.')


class Lnode:
    def __init__(self,data,Last):
        self.data = data
        self.Last = Last

    def make_empty():
        self.data = []
        self.Last = -1
        return

    def find(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1

    def insert(self, index, value):
        if index >= self.Last:
            print('位置不合法')
            return
        else:
            self.data += ' '
            for i in range(self.Last,index, -1):
                self.data[i] = self.data[i-1]
            self.data[index] = value
            self.Last += 1
            return

    def delete(self, index):
        if index < 0 or index >= self.Last:
            print('位置不合法')
            return
        else:
            for i in range(index,self.Last-1):
                self.data[i] = self.data[i+1]
            del self.data[self.Last - 1]
            self.Last -= 1
            return

class Lnode2:
    def __init__(self, data):
        self.data = data
    def length(self):
        return self.data.get_length()

    def findKth(self,k):
        node = self.data.head
        i = 1
        while node and i < k:
            node = node.next
            i += 1
        if i == k:
            return node.data
        else:
            return None
    def find(self, value):
        node = self.data.head
        while node and node.data != value:
            node = node.next
        return node
    def insert(self, value, index):
        self.data.insert(value, index)
        return
    def delete(self, index):
        self.data.delete(index)
        return

class Snode:
    def __init__(self):
        self.data = []
        self.top = len(self.data) - 1

    def is_empty(self):
        return self.top == -1


    def push(self, value):
        self.data.append(value)
        self.top += 1
        return

    def pop(self):
        if self.top == -1:
            return None
        else:
            node = self.data[self.top]
            del self.data[self.top]
            self.top -= 1
            return node

class Snode2:
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
            value = node.data
            self.head = self.head.next
            del node
            self.length -= 1
            return value

    def show_all(self):
        if self.is_empty():
            #print('堆栈为空')
            return
        else:
            node = self.head
            print(node.data, end=' ')
            while node.next:
                node = node.next
                print(node.data, end=' ')
            print('None')



if __name__ == '__main__':
    #node1 = Node('node1')
    #node2 = Node('node2')
    #linked_list = LinkedList()
    #linked_list.append(node1)
    #linked_list.append(node2)
    #linked_list.print_linked_list()
    #linked_list.insert('node2.5', 1)
    #linked_list.print_linked_list()
    #a = [1,2,3,'wwwuwuu']
    #lnode = Lnode(a, len(a))

    #index = lnode.find(2)

    #print(index)

    #print(lnode.data)
    #lnode.insert(1,10)
    #print(lnode.data)
    #lnode.insert(2,20)
    #print(lnode.data)
    #lnode.delete(1)
    #print(lnode.data)

    llist = LinkedList()
    llist.append('I')
    llist.append('hate')
    llist.append('you')
    #llist.print_linked_list()

    #prtl = Lnode2(llist)
    #prtl.data.print_linked_list()
    #print(prtl.findKth(2))
    #print(prtl.find('youu'))
    #prtl.insert('love', 1)
    #prtl.data.print_linked_list()
    #prtl.delete(1)
    #prtl.data.print_linked_list()
    #snode = Snode()
    #snode.push('nice')
    #print(snode.data)
    #snode.push('to')
    #print(snode.data)
    #key = snode.pop()
    #print(key)
    #print(snode.data)

    #snode = Snode2()
    #snode.push('you')
    #snode.push('dont')
    #snode.push('like')
    #snode.push('it')
    #snode.pop()
    #snode.show_all()

    content = list('(1.2 + 1.3 - 2) * 4.2')
    signal = ")(+-*/ "
    equation = Snode2()
    number = Snode2()
    i = 0
    while i < len(content):
        if content[i] not in signal:
            number.push(content[i])
        else:
            if number.length:
                shuzi = []
                while number.length:
                    shuzi += number.pop()
                shuzi.reverse()
                equation.push(''.join(shuzi))
            equation.push(content[i])
        i += 1
    if number.length:
        shuzi = []
        while number.length:
            shuzi.append(number.pop())
        shuzi.reverse()
        equation.push(''.join(shuzi))
    expressions = []
    while equation.length:
        value = equation.pop()
        if value != ' ':
            expressions.append(value)
    expressions.reverse()







