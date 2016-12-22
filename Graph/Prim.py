import GraphBase
import PFS
VStatus = GraphBase.VStatus
EStatus = GraphBase.EStatus


class Prim(PFS.PFS):

    def __init__(self, g):
        PFS.PFS.__init__(self, g)

    def prim(self, s):
        PFS.PFS.pfs(self, s)

    def relaxation(self, e, s):
        if g.vertices[e.toIndex].status == VStatus.Undiscovered and g.vertices[e.toIndex].priority > e.weight:
            g.vertices[e.toIndex].priority = e.weight
            g.vertices[e.toIndex].parent = s

if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    e = [(0, 1, 6), (0, 2, 12), (1, 2, 5), (2, 3, 9), (1, 4, 14), (2, 5, 7), (1, 7, 8), (5, 6, 15), (4, 7, 3), (5, 7, 10)]
    g = GraphBase.GraphBase()
    g.buildGraph(v, e, False)
    g.printAdj()
    p = Prim(g)
    p.prim(5)
    p.printVertices()
