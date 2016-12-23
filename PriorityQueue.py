#vim: set fileencoding:utf-8
import Utils


class PriorityQueue(object):

    def __init__(self, vec):
        self._size = len(vec)
        self._elem = vec[:]
        self.heapify(len(vec))

    def __len__(self):
        return self._size

    def parent(self, i):
        return (i-1)/2

    def lChild(self, i):
        return 2*i+1

    def rChild(self, i):
        return 2*(i+1)

    def hasParent(self, i):
        return i > 0

    def inHeap(self, i, n):
        return -1 < i < n

    def hasLChild(self, i, n):
        return self.inHeap(self.lChild(i), n)

    def hasRChild(self, i, n):
        return self.inHeap(self.rChild(i), n)

    def lastInternal(self, n):
        'last internal node is the parent of last node'
        return self.parent(n-1)

    def lessThan(self, i, j):
        return self._elem[i] < self._elem[j]

    def biggerIndex(self, i, j):
        if self.lessThan(i, j):
            return j
        return i

    def properParent(self, i, n):
        if self.hasRChild(i, n):
            return self.biggerIndex(self.biggerIndex(i, self.lChild(i)), self.rChild(i))
        elif self.hasLChild(i, n):
            return self.biggerIndex(i, self.lChild(i))
        else:
            return i

    def swap(self, i, j):
        self._elem[i], self._elem[j] = self._elem[j], self._elem[i]

    def heapify(self, n):
        for i in range(self.lastInternal(n), -1, -1):
            self._heapDown(i, n)

    def _heapUp(self, i):
        while self.hasParent(i) and not self.lessThan(i, self.parent(i)):
            j = self.parent(i)
            self.swap(i, j)
            i = j
        return i

    def _heapDown(self, i, n):
        j = self.properParent(i, n)
        while not i == j:
            self.swap(i, j)
            i = j
            j = self.properParent(i, n)
        return i

    def insertHeap(self, e):
        self._elem.append(e)
        self._size += 1
        self._heapUp(self._size - 1)

    def getMax(self):
        if self.isEmpty():
            raise Utils.Empty('queue is empty')
        return self._elem[0]

    def delMax(self):
        ret = self._elem[0]
        self._size -= 1
        self._elem[0] = self._elem[self._size]
        self._elem[self._size] = None
        self._heapDown(0, self._size)
        return ret

    def isEmpty(self):
        return self._size <= 0

    def printAll(self):
        print ("****************** pq's size == %s ******************" % str(self._size))
        self.printHeap(self._size, 0, 0, Utils.NodeType.Root, {})

    def _getData(self, k):
        return self._elem[k]

    def printHeap(self, n, k, depth, type, bTypes):
        if k >= n:
            return
        bTypes[depth] = type
        self.printHeap(n, self.rChild(k), depth + 1, Utils.NodeType.RC, bTypes)
        print "%-20s" % str(self._getData(k)),
        for i in range(depth):
            if bTypes[i] + bTypes[i+1]:
                print "      ",
            else:
                print "│    ",
        if type == Utils.NodeType.RC:
            print "┌──",
        elif type == Utils.NodeType.LC:
            print "└──",
        else:
            "──",
        print self._getData(k)
        self.printHeap(n, self.lChild(k), depth + 1, Utils.NodeType.LC, bTypes)

if __name__ == '__main__':
    a = [1, 3, 4, 99, 10, 65, 20, 7]
   # a = [1, 2, 3]
    pq = PriorityQueue(a)
    pq.insertHeap(88)
    pq.printAll()
    pq.delMax()
    pq.printAll()
    pq.delMax()
    pq.printAll()
    pq.delMax()
    pq.delMax()
    pq.delMax()

    pq.printAll()

