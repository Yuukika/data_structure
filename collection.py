class Node:
    def __init__(self, data, parent=-1):
        self.data = data
        self.parent = parent




class Collection:
    def __init__(self):
        self.data = []
    def create(self):
        self.data.append(Node(1,-1))
        self.data.append(Node(2,0))
        self.data.append(Node(3,-1))
        self.data.append(Node(4,0))
        self.data.append(Node(5,2))
        self.data.append(Node(6,-1))
        self.data.append(Node(7,0))
        self.data.append(Node(8,2))
        self.data.append(Node(9,5))
        self.data.append(Node(10,5))
        for item in self.data:
            if item.parent < 0:
                for element in self.data:
                    if self.data[element.parent] == item:
                        item.parent -= 1
        return

    def find(self, x):
        i = 0
        while i<len(self.data) and self.data[i].data != x:
            i = i+1
        if i >= len(self.data):
            return None
        while self.data[i].parent>=0:
            i = self.data[i].parent
        return i

    def union(self,x1, x2):
        root1 = self.find(x1)
        root2 = self.find(x2)
        if root1 != root2:
            sum = self.data[root1].parent + self.data[root2].parent
            if self.data[root2].parent <= self.data[root1].parent:
                self.data[root1].parent = root2
                self.data[root2].parent = sum
            else:
                self.data[root2].parent = root1
                self.data[root1].parent = sum
    def show_all(self):
        for item in self.data:
            print(item.parent,' ')
if __name__ == '__main__':
    a = Collection()
    a.create()
    a.union(2,5)
    a.show_all()
