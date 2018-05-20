#!/usr/bin/env python
# -*-coding:utf-8-*-



"""
1、n个顶点的强连通图至少有多少条边？这样的有向图是什么形状?
强连通图是指有向图中任意两个顶点都连通，那么每个顶点度至少要大于等于2，n
个顶点的图至少有n条边，这样的图形成一个环。第一个顶点到第二个顶点有一条有向边，第二个顶点
到第三个顶点有一条有向边，最后一个顶点到第一个顶点有一个有向边。
2、给定一个具有n个节点的无向图的邻接矩阵和邻接表：
    设计一个将邻接矩阵转换为邻接表的算法
    设计一个将邻接表转换为邻接矩阵的算法
    分析上述两个算法的时间复杂度
3、假设图G采用邻接表存储，设计一个算法，判断无向图G是否连通。若连通返回1，否则返回0
4、假设图G采用邻接表存储，设计一个算法，输出图G中从顶点u到v的长度为l的所有简单路径。
5、假设图G采用邻接表存储，设计一个算法，求图中通过某顶点k的所有简单回路（若存在）。
并输出有向图的邻接表和通过顶点0的所有回路。
6、
"""
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

    def is_empty(self):
        return self.length == 0
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

class Edge():
    """
    边的定义
    """
    def __init__(self,V1,V2,weight):
        self.V1 = V1
        self.V2 = V2
        self.weight = weight

class Graph:
    """
    图的定义:以邻间矩阵来存储
    特点：
        图的邻间矩阵表示是唯一的
        图的邻间矩阵是一个对称的矩阵
        邻间矩阵第i行或列上的非零元素的个数正好是第i个顶点的度
    """
    def __init__(self,VertexNum):
        """
        初始化一个有VertexNum个顶点但没有边的图
        """
        self.Nv = VertexNum #顶点数
        self.Ne = 0 #弧数
        self.Glist = [[65535 for i in range(VertexNum)] for i in range(VertexNum)]#邻间矩阵
        self.data = [] #存储顶点数据
        self.visited = [False for i in range(VertexNum)]
    def insertedge(self, edge):

        # 插入边<V1,V2>
        self.Glist[edge.V1][edge.V2] = edge.weight
        # 若是无向边,还要插入边<V2,V1>
        self.Glist[edge.V2][edge.V1] = edge.weight

    def buildgraph(self):
        self.Ne = int(input("输入图的边个数:"))
        if self.Ne != 0:
            for i in range(self.Ne):
                V1,V2,weight = eval(input('输入边的顶点和权重:'))
                edge = Edge(V1,V2,weight)
                self.insertedge(edge)

        for i in range(self.Nv):
            self.data.append(eval(input("请依次输入顶点的数据:")))

    def isedge(self,V1,V2):
        return True if self.Glist[V1][V2] != 0 else False

    def visit(self, vertex):
        print('正在访问顶点{0}'.format(vertex))

    def BFS(self, vertex):
        """
        首先访问初始点v,接着访问v的所有未被访问过的邻接点,然后按照顶点的次序访问每一个顶点的所有未被访问过的
        邻接点，此次类推，直到图中额所有和初始点v有路径相同的顶点都被访问过为止。
        """
        Q = Qnode(10)
        self.visit(vertex)
        self.visited[vertex] = True
        Q.addq(vertex)

        while not Q.is_empty():
            V = Q.deleteq()
            for W in range(self.Nv):
                if not self.visited[W] and self.isedge(V,W):
                    self.visit(W)
                    self.visited[W] = True
                    Q.addq(W)

class AdjVNode:
    """
    邻间节点
    """
    def __init__(self, AdjV, weight):
        self.AdjV = AdjV
        self.weight = weight
        self.next = None

class Vnote:
    """
    表头节点
    """
    def __init__(self,data):
        self.next = None
        self.data = data

    def __repr__(self):
        return str(self.data)

class LGraph:
    """
    采用邻间表的形式构造图
    特点：
    不唯一，每个顶点的链表顺序可以任意。
    n个顶点和e条边的无向图，邻间表有n个顶点，2e个边节点
    邻间表的顶点对应的链表的边节点个数就是该顶点的度
    有向图中邻间表的顶点对应的链表的边节点个数就是该顶点的出度
    入度为图中所有邻间节点的adjV指向该顶点的数目
    """
    def __init__(self, VertexNum):
        """
            初始化一个具有vertexnum节点的图
        """
        self.Nv = VertexNum
        self.Ne = 0
        self.Glist = [Vnote(i) for i in range(VertexNum)]
        self.data = []
        self.visited = [False for i in range(VertexNum)]l
    def insertedge(self, edge):
        # 有向图插入新的邻接点
        # 创建邻间节点
        Node = AdjVNode(edge.V2, edge.weight)
        # 在邻间表的对应节点处插入邻接点
        Node.next = self.Glist[edge.V1].next
        self.Glist[edge.V1].next = Node

        # 无向图插入邻接点
        #Node = AdjVNode(edge.V1, edge.weight)
        #Node.next = self.Glist[edge.V2].next
        #self.Glist[edge.V2].next = Node

    def buildgraph(self):
        self.Ne = int(input("输入图的边个数:"))
        if self.Ne != 0:
            for i in range(self.Ne):
                V1,V2,weight = eval(input('输入边的顶点和权重:'))
                edge = Edge(V1,V2,weight)
                self.insertedge(edge)

        for i in range(self.Nv):
            self.data.append(eval(input("请依次输入顶点的数据:")))

    def visit(self, vertex):
        print('正在访问顶点{0}'.format(vertex))
    def DFS(self, vertex):
        """
        从图中某个初始顶点v出发，首先访问初始顶点v,然后选择一个与顶点v相邻且没有被访问过的顶点w为初始顶点
        再从w出发进行深度优先搜索，直到图中与当前顶点v邻接的所有顶点都被访问过为止。
        """
        self.visit(vertex)
        self.visited[vertex] = True

        Node = self.Glist[vertex].next
        while Node:
            if not self.visited[Node.AdjV]:
                self.DFS(Node.AdjV)
            Node = Node.next
    def DFS2(self,vertex):
        Q = Qnode(self.Nv)
        self.visit(vertex)
        self.visited[vertex] = True
        Q.addq(vertex)
        while not Q.is_empty():
            V = Q.deleteq()
            node = self.Glist[vertex].next
            while node:
                if not self.visited[node.AdjV]:
                    self.visit(node.AdjV)
                    self.visited[node.AdjV]
                    Q.addq(node.AdjV)
                node = node.next
