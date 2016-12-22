import sys
import DoublyLinkedList
import LinkedListQueue


class VStatus(object):
    Undiscovered = 0
    Discovered = 1
    Visited = 2


class EStatus(object):
    Undetermined = 0
    Tree = 1
    Cross = 2
    Forward = 3
    BackWard = 4


class Vertex(object):

    def __init__(self, data):
        self.data = data
        self.inDegree = self.outDegree = 0
        self.status = VStatus.Undiscovered
        self.dTime = self.fTime = -1
        self.parent = -1
        self.priority = sys.maxint

    def __eq__(self, other):
        return


class Edge(object):

    def __init__(self, fromV, toV, weight=1, data=None):
        self.fromIndex, self.toIndex = fromV, toV
        self.data, self.weight = data, weight
        self.type = EStatus.Undetermined


class GraphBase(object):

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adj = []

    def vCount(self):
        return self.vertices.__len__()

    def buildGraph(self, vertices, edges, directed=True):
        for i in vertices:
            self.insertVertex(i)
        for i in edges:
            weight = i[2] if i.__len__() > 2 else 1
            self.adj[i[0]].insertAsFirst(Edge(i[0], i[1], weight))
            self.vertices[i[0]].outDegree += 1
            self.vertices[i[1]].inDegree += 1
            if not directed:
                self.adj[i[1]].insertAsFirst(Edge(i[1], i[0], weight))
                self.vertices[i[1]].outDegree += 1
                self.vertices[i[0]].inDegree += 1

    def getEdge(self, f, t):
        for i in self.adj[f]:
            if i.data.toIndex == t:
                return i.data

    def insertVertex(self, e):
            v = Vertex(e)
            self.vertices.append(v)
            self.adj.append(DoublyLinkedList.DoublyLinkedList())
            return v

    def reset(self):
        for v in self.vertices:
            v.inDegree = v.outDegree = 0
            v.dTime = v.fTime = -1
            v.parent = -1
            v.priority = sys.maxint
        for a in self.adj:
            for node in a:
                node.data.type = EStatus.Tree

    def XFS(self, s, xfs, visit=None):
        self.reset()
        clock = 0
        v = s
        while True:
            if self.vertices[v].status == VStatus.Undiscovered:
                clock = xfs(v, clock, visit)
            v = (v + 1) % self.vertices.__len__()
            if v == s:
                break

    def visitVertex(self, v, visit):
        self.vertices[v].status = VStatus.Discovered
        if visit and hasattr(visit, '__call__'):
            visit(self.vertices[v])
        else:
            print self.vertices[v].data

    def DFS(self, s, visit=None):
        self.XFS(s, self.dfs, visit)

    def dfs(self, v, clock, visit=None):
        clock += 1
        self.vertices[v].dTime += clock
        self.visitVertex(v, visit)
        for i in self.adj[v]:
            vto = self.vertices[i.data.toIndex]
            if vto.status == VStatus.Undiscovered:
                i.type = EStatus.Tree
                clock = self.dfs(i.data.toIndex, clock)
                vto.parent = v
            elif vto.status == VStatus.Discovered:
                i.type = EStatus.BackWard
            else:
                i.type = EStatus.Forward if self.vertices[v].dTime < vto.dTime else EStatus.Cross
        self.vertices[v].status = VStatus.Visited
        clock += 1
        self.vertices[v].fTime = clock
        return clock

    def BFS(self, s, visit=None):
        self.XFS(s, self.bfs, visit)

    def bfs(self, v, clock, visit=None):
        queue = LinkedListQueue.LinkedListQueue()
        queue.enqueue(v)
        while not queue.isEmpty():
            v = queue.dequeue().data
            self.visitVertex(v, visit)
            clock += 1
            self.vertices[v].dTime += clock
            for i in self.adj[v]:
                vto = self.vertices[i.data.toIndex]
                if vto.status == VStatus.Undiscovered:
                    i.type = EStatus.Tree
                    vto.parent = v
                    print "enqueue" + str(i.data.toIndex)
                    vto.status = VStatus.Discovered
                    queue.enqueue(i.data.toIndex)
                else:
                    i.type = EStatus.Cross
            self.vertices[v].status = VStatus.Visited


    def printAdj(self):
        index = 0
        for i in self.vertices:
            print "%s  %s:    " % (str(index), str(i.data)),
            jIndex = 0
            for j in self.adj[index]:
                print j.data.toIndex,
                if not jIndex == self.adj[index].__len__()-1:
                    print " -->",
                jIndex += 1
            print ""
            index += 1


if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e', 'g']
    e = [(0, 5), (2, 4), (2, 3), (1, 2), (0, 1), (3, 4), (3, 5), (0, 2)]
    g = GraphBase()
    g.buildGraph(v, e, True)
    g.printAdj()
    g.BFS(0, 0)
    print g
