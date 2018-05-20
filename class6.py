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
    主要操作包括：初始化图Create,
    clearGraph销毁图,
    InsertVertex,
    InsertEdge,
    DFS(从顶点V出发深度优先遍历图G)
    BFS广度优先遍历图,
    ShortestPath,
     MST等

基本术语：
    端点，邻接点
    (v1,v2)是一条边，则称v1,v2是该边的两个端点，v1,v2互为邻接点
    <v1,v2>有向边,v1指向v2,该边是v1的一条出边，相应的是v2的入边，v1，v2是该边的起始端点和终止端点
    v1,v2互为邻接点，称v2是v1的出边邻接点，v2是v1的入边邻接点

    顶点的度、入度和出度
    在无向图中，顶点具有的边的个数称为该顶点的度
    出度：在有向图中，以该顶点为起点的出边的数目是该顶点的出度，反之为入度。一个顶点的度等于出度和入度的和。

    完全图
    无向图中每两个顶点都存在着一条边
    有向图中每两个顶点都存在着方向相反的两条边，那么该图就是完全图
    n个结点的无向完全图共有n(n-1)/2条边，有向完全图共有n(n-1)条边

    稠密图，稀疏图
    边多的接近完全图的叫做稠密图，边少的叫稀疏图

    子图
    两个图，一个图的端点和边集合都是另一个图的端点边集合的子集，则称该图为另一个图的子图

    路径和路径长度
    在图中，一个顶点到另一个顶点的边集合称为路径，在有向图中则为有向路径。
    路径长度是一个路径上边的数目。
    如果V到W之间的所有顶点都不同，则称简单路径.

    回路或环
    在一条路径上，起点和终点为同一端点的路径称为回路或环
    如果该路径为简单路径，则称为简单回路或简单环

    连通
    如果从V到W存在一条（无向）路径，则称V和W是连通的
    连通图
    图中任意两个端点都连通的图称为连通图

    连通分量：五向图的极大连通子图
    极大顶点数：再加1个顶点就不连通了
    极大边数：包含子图中所有顶点相连的所有边

    强连通：有向图中顶点V和W之间存在双向路径，则称V和W是强连通的

    强连通图：有向图中任意两顶点均强连通

    强连通分量：有向图的极大强连通子图

    关节点， 重连通图
    删除图中一个顶点和相关联的各边后，将图的一个连通分量分割成两个或多个连通分量，则称该节点是该图的一个关节点。
    一个没有关节点的连通图称为重连通图

    权和网
    图中每条边都赋予值，这个值就叫边的权，带权的图称为网


用邻间矩阵来表示G[N][N]来表示顶点之间的边的关系，如果两个顶点之间有边那么对应的点为1，带权的则表示为对应数值，否则为零

也可以用长度为(n*(n+1)/2)的数组来表示图Gij,那么某个顶点对应与数组中的点为(i*(i+1)/2 + j)

邻间矩阵的优点是：
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

其他的存储方法还有：十字邻间表，邻接多重表

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
        self.path = [-1 for i in range(VertexNum)]
        self.dist = [65535 for i in range(VertexNum)]
        self.collected = [False for i in range(self.Nv)]
        self.D = self.Glist
        self.Dpath = [[-1 for i in range(VertexNum)] for i in range(VertexNum)]
        self.parent = [0 for i in range(VertexNum)]
        self.MST = LGraph(self.Nv)

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

    def floyd(self):
        """
        有权图的单源最短路算法:
        有向图G(V,E)采用邻间矩阵存储，D二维数组存放当前顶点之间的最短路径长度
        递归的产生一个矩阵序列，A0,A1...Ak...An,其中Ak[i][j]表示从顶点Vi到顶点Vj的路径上所经过
        的顶点编号不大于k的最短路径长度。
        """
        self.D = self.Glist
        for i in range(self.Nv):
            for j in range(self.Nv):
                for k in range(self.Nv):
                    if self.D[i][k] + self.D[k][j] < self.D[i][j]:
                        self.D[i][j] = self.D[i][k] + self.D[k][j]
                        if i==j and self.D[i][j] < 0:
                            return False
                        self.Dpath[i][j] = k
        return True



    def findmindist(self):
        """
        从未收录collected的顶点中dist最小的值
        """
        Mindist = 65535
        for V in range(self.Nv):
            if not self.collected[V] and self.dist[V] < 65535:
                Mindist = self.dist[V]
                MinV = V
        if Mindist < 65535:
            return MinV
        else:
            return None


    def Dijkstra(self,vertex):
        """
        狄克斯特拉算法：带权的单源最短路径算法
        基本思想是:G(V,E)为一个带权有向图，把图中顶点集合分成两组
        第一组为已求出最短路径的顶点集合，初始时只有源节点，以后每求出一条最短路径，将该节点加入到集合中
        第二组是其余未求出最短路径的顶点集合，按最短路径长度增次序依次将顶点加入到第一组当中去。
        """
        for i in range(self.Nv):
            # 初始化顶点的路径，如果是初始节点的邻接节点，则设置对应的路径为初始节点，反之为-1
            self.dist[i] = self.Glist[vertex][i]
            if self.dist[i] < 65535:
                self.path[i] = vertex
            else:
                self.path[i] = -1
        #初始节点对应的距离为0
        self.dist[vertex] = 0
        # 把初始节点收入到集合中
        self.collected[vertex] = True

        while True:
            # 从未被收入集合的顶点中找到最小dist点
            V = self.findmindist()
            # 如果不存在，跳出算法
            if not V:
                break
            # 将该节点收入集合
            self.collected[V] = True
            # 遍历每个顶点，更新距离和路径
            for i in range(self.Nv):
                # 如果连个节点是邻接点且未被收录
                if not self.collected[i] and self.Glist[V][i] < 65535:
                    # 如果有负边，该算法无法解决，返回false
                    if self.Glist[V][i] < 0:
                        return False
                    # 如果收录该节点使得最小距离变小，更新最小距离和路径
                    if self.dist[V]+self.Glist[V][i] < self.dist[i]:
                        self.dist[i] = self.dist[V] + self.Glist[V][i]
                        self.path[i] = V

        return True

    def findmindist2(self):
        Mindist = 65535
        for V in range(self.Nv):
            # 未被收录且到生成树的距离更小的顶点
            if self.dist[V] != 0 and self.dist[V] < Mindist:
                Mindist = self.dist[V]
                MinV = V

        if Mindist < 65535:
            return MinV
        else:
            return None


    def prim(self):
        """
        无向有权图生成最小生成树的算法
        """
        # 初始化所有顶点和初始节点的距离
        for i in range(self.Nv):
            self.dist[i] = self.Glist[0][i]
            #dist数组记录的所有顶点到生成树的最短距离，如果不是生成树的邻间节点，则表示距离为65535
        # 生成树的总权重
        TotalWeight = 0
        # 生成树的收录节点数
        VCount = 0
        # 将初始节点收录到生成树当中
        self.dist[0] = 0
        VCount += 1
        self.parent[0] = -1

        while True:
            V = self.findmindist2()
            if not V:
                break
            # 生成边，插入到MST
            edge = Edge(self.parent[V], V,self.dist[V])
            self.MST.insertedge(edge)
            TotalWeight += self.dist[V]
            self.dist[V] = 0
            VCount += 1
            # 更新未被收录的节点到生成树的距离及父节点
            for W in range(self.Nv):
                if self.dist[W] != 0 and self.Glist[V][W] < 65535:
                    if self.Glist[V][W] < self.dist[W]:
                        self.dist[W] = self.Glist[V][W]
                        self.parent[W] = V
        if VCount < self.Nv:
            TotalWeight  = None

        return TotalWeight






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
        self.visited = [False for i in range(VertexNum)]
        self.path = [-1 for i in range(VertexNum)]
        self.dist = [-1 for i in range(VertexNum)]

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



    def unweighted(self,vertex):
        Q = Qnode(self.Nv)
        self.dist[vertex] = 0
        Q.addq(vertex)
        while not Q.is_empty():
            V = Q.deleteq()
            node = self.Glist[V].next
            while node:
                if self.dist[node.AdjV] == -1:
                    self.dist[node.AdjV] = self.dist[V] + 1
                    self.path[node.AdjV] = V
                    Q.addq(node.AdjV)
                node = node.next




if __name__ == '__main__':
    graph = Graph(5)
    graph.buildgraph()
    #graph.unweighted(0)











