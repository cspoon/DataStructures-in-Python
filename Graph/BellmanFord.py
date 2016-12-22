import GraphBase
import sys

class BellmanFord(object):

    def __init__(self, g):
        self.g = g

    def bellmanFord(self, s):
        g = self.g
        g.reset()
        g.vertices[s].priority = 0
        for i in range(g.vCount()-1):
            for e in g.edges:
                if not e.fromIndex == sys.maxint \
                        and g.vertices[e.toIndex].priority > g.vertices[e.fromIndex].priority + e.weight:
                    g.vertices[e.toIndex].priority = g.vertices[e.fromIndex].priority + e.weight
                    g.vertices[e.toIndex].parent = e.fromIndex
        for e in g.edges:
            if g.vertices[e.toIndex].priority > g.vertices[e.fromIndex].priority + e.weight:
                print ("there is a negative ring in graph~!")

    def printVertices(self):
        index = 0
        vertices = self.g.vertices
        for v in range(self.g.vCount()):
            print "%s(%s).priority: %s   " % (str(v), str(vertices[v].data), str(vertices[v].priority)),
            print "%s(%s).parent: %s" % (str(v), str(vertices[v].data),
                                         str(vertices[vertices[v].parent].data) if not vertices[
                                                                                           v].parent == -1 else "None")

if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e']
    e = [(1, 4, 2), (3, 1, 1), (1, 3, 2), (0, 1, -1), (0, 2, 4), (3, 2, 5), (1, 2, 3), (4, 3, -3)]
    g = GraphBase.GraphBase()
    g.buildGraph(v, e)
    g.printAdj()
    d = BellmanFord(g)
    d.bellmanFord(0)
    d.printVertices()



