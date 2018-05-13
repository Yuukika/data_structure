#!/usr/bin/env python
# -*-coding:utf-8-*-




"""

图： graph 表示“多对多”的关系
一般包含：
一组顶点：通常用V（Vertex）表示定点集合
一组边：通常用E(Edge)表示边的集合
边是顶点对:(v,w) 属于E,其中v,w都是顶点,括号表示无向边
<v,w>表示v指向w的边(单行线)
不考虑重边和自回路


图的抽象数据类型定义:
类型名称：图(graph)
数据对象集：G(V,E)由一个非空的有限顶点集合V和一个有限边集合E组成
主要操作包括：Create,InsertVertex, InsertEdge, DFS(从顶点V出发深度优先遍历图G)
BFS， ShortestPath, MST等



用邻间矩阵来表示G[N][N]来表示顶点之间的边的关系，如果两个顶点之间有边那么对应的点为1，否则为零

也可以用长度为(n*(n+1)/2)的数组来表示图Gij,那么某个顶点对应与数组中的点为(i*(i+1)/2 + j)

邻间矩阵的有点是：
直观，简单，好理解
方便检查任意一对顶点间是否存在边
方便找任意顶点的所有"邻接点"(有边直接相连的点)
方便计算任一顶点的”度“(从该点发出的边数为”出度“，指向改点的边数为”入度“)
    无向图：对应行（或列）非0元素的个数
    有向图：对应行非0元素的个数是”出度“；对应列非零元素的个数是”入度“
邻间矩阵的缺点：
浪费空间，如果图里顶点很多而边很少，那么就会造成空间浪费
浪费事件，统计稀疏图中的边个数

用邻间表来表示一个图，G[N]为指针数组，对应矩阵每行一个链表，只存非0元素
优点：
方便找任一顶点的所有邻接点
节约稀疏图的空间：需要N个头指针，2E个结点

方便计算任一顶点的”度“：
    对无向图可以实现
    对有向图来说，只能计算”出度“，需要构造”逆邻接表“(存指向自己的边)来方便计算"r入度"

不方便检查任意一对顶点间是否存在边



图的遍历有两种方法：1、深度优先搜索DFS 2、广度优先搜索BFS


连通：如果从V到W存在一条（无向）路径，则称V和W是连通的

路径：V到W的路径是一系列顶点的集合，其中任一对相邻的顶点间都是土中的边。
路径的长度是路径中的边数(如果带权，则是所有边的权重和)。
如果V到W之间的所有顶点都不同，则称简单路径.
回路：七点等于终点的路径
连通图：图中任意两顶点都连通

连通分量：五向图的极大连通子图
极大顶点数：再加1个顶点就不连通了
极大边数：包含子图中所有顶点相连的所有边

强连通：有向图中顶点V和W之间存在双向路径，则称V和W是强连通的

强连通图：有向图中任意两顶点均强连通

强连通分量：有向图的极大强连通子图

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
    """
    def __init__(self,VertexNum):
        """
        初始化一个有VertexNum个顶点但没有边的图
        """
        self.Nv = VertexNum
        self.Ne = 0
        self.Glist = [[0 for i in range(VertexNum)] for i in range(VertexNum)]
        self.data = []
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
    def __init__(self, AdjV, weight):
        self.AdjV = AdjV
        self.weight = weight
        self.next = None

class Vnote:
    def __init__(self,data):
        self.next = None
        self.data = data

    def __repr__(self):
        return str(self.data)

class LGraph:
    """
    采用邻间表的形式构造图
    """
    def __init__(self, VertexNum):
        self.Nv = VertexNum
        self.Ne = 0
        self.Glist = [Vnote(i) for i in range(VertexNum)]
        self.data = []
        self.visited = [False for i in range(VertexNum)]

    def insertedge(self, edge):
        # 有向图插入新的邻接点
        Node = AdjVNode(edge.V2, edge.weight)
        Node.next = self.Glist[edge.V1].next
        self.Glist[edge.V1].next = Node

        # 无向图插入邻接点
        Node = AdjVNode(edge.V1, edge.weight)
        Node.next = self.Glist[edge.V2].next
        self.Glist[edge.V2].next = Node

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
        self.visit(vertex)
        self.visited[vertex] = True

        Node = self.Glist[vertex].next
        while Node:
            if not self.visited[Node.AdjV]:
                self.DFS(Node.AdjV)
            Node = Node.next


if __name__ == '__main__':
    graph = Graph(4)
    graph.buildgraph()
    graph.BFS(0)











