import PriorityQueue


class AdaptablePriorityQueue(PriorityQueue.PriorityQueue):

    class Locator:

        def __init__(self, e, index):
            self.e = e
            self.index = index

    def __init__(self, vec):
        self._size = len(vec)
        self._elem = []
        for i in range(self._size):
            self._elem.append(self.Locator(vec[i], i))
        self.heapify(self._size)

    def lessThan(self, i, j):
        return self._elem[i].e < self._elem[j].e

    def swap(self, i, j):
        PriorityQueue.PriorityQueue.swap(self, i, j)
        self._elem[i].index, self._elem[j].index = self._elem[j].index, self._elem[i].index

    def _bubble(self, i, n):
        if self.hasParent(i) and self.lessThan(i, self.parent(i)):
            self._heapUp(i)
        else:
            self._heapDown(i, n)

    def insert(self, e):
        token = self.Locator(e, self._size)
        self._elem.append(token)
        self._size += 1
        self._heapUp(self._size - 1)
        return token

    def update(self, loc, newE):
        if not loc:
            raise Exception('loc is null')
        if not(-1 < loc.index < self._size and self._elem[loc.index] is loc):
            raise ValueError('invalid locator')
        loc.e = newE
        self._bubble(loc.index, self._size-1)

    def remove(self, loc):
        if not loc:
            raise Exception('loc is null')
        if not (-1 < loc.index < self._size and self._elem[loc.index] is loc):
            raise ValueError('invalid locator')
        self._size -= 1
        loc.e = self._elem[self._size].e
        self._elem[self._size] = None
        self._bubble(loc.index, self._size)
        return loc

    def printAll(self):
        ret = []
        while not self.isEmpty():
            ret.append(self.delMax().e)
        print ret

if __name__ == '__main__':
    a = [1, 3, 4, 99, 10, 65, 20, 7]
    # a = [1, 2, 3]
    pq = AdaptablePriorityQueue(a)
    n = pq.insert(100)
    pq.remove(n)

    pq.printAll()
