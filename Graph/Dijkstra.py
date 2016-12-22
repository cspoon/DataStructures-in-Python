import GraphBase
import PFS
VStatus = GraphBase.VStatus
EStatus = GraphBase.EStatus


class Dijkstra(PFS.PFS):

    def __init__(self, g):
        PFS.PFS.__init__(self, g)

    def dijkstra(self, s):
        PFS.PFS.pfs(self, s)

    def relaxation(self, e, s):
        vertices = g.vertices
        if vertices[e.toIndex].status == VStatus.Undiscovered \
                and vertices[e.toIndex].priority > vertices[s].priority + e.weight:
            vertices[e.toIndex].priority = vertices[s].priority + e.weight
            vertices[e.toIndex].parent = s

if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e']
    e = [(1, 3, 2), (0, 1, 10), (1, 2, 1), (2, 1, 4), (2, 3, 8), (3, 4, 7), (4, 3, 9), (0, 2, 3), (2, 4, 2)]
    g = GraphBase.GraphBase()
    g.buildGraph(v, e)
    g.printAdj()
    d = Dijkstra(g)
    d.dijkstra(0)
    d.printVertices()
