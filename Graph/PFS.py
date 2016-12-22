import GraphBase
import sys
VStatus = GraphBase.VStatus
EStatus = GraphBase.EStatus


class PFS(object):
    'priority first search'
    def __init__(self, g):
        self.g = g
        self.visit = None

    def pfs(self, s):
        g = self.g
        g.reset()
        g.vertices[s].priority = 0
        for i in range(g.vCount()):
            g.vertices[s].status = VStatus.Visited
            if self.visit:
                self.visit(g.vertices[s])
            if not g.vertices[s].parent == -1:
                e = g.getEdge(g.vertices[s].parent, s)
                e.type = EStatus.Tree
            for j in g.adj[s]:
                self.relaxation(j.data, s)
            s = self.getMinPriorityVertex()

    def relaxation(self, e):
        pass

    def getMinPriorityVertex(self):
        '''
        this operation can improve to other data structures:
        array               O(v^2)
        binary heap         O(elgv)
        Fib heap            O(vlgv + e)(worst case)
        '''
        min = sys.maxint
        ret = -1
        for i in range(self.g.vCount()):
            if self.g.vertices[i].status == VStatus.Undiscovered and self.g.vertices[i].priority < min:
                min = self.g.vertices[i].priority
                ret = i
        return ret

    def printVertices(self):
        index = 0
        vertices = self.g.vertices
        for v in range(self.g.vCount()):
            print "%s(%s).parent: %s" % (str(v), str(vertices[v].data), str(vertices[vertices[v].parent].data) if not vertices[v].parent == -1 else "None")