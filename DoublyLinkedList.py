

class DoublyLinkedList:

    class Node(object):
        def __init__(self, e, p, s, list):
            self.data, self.pred, self.succ, self.list = e, p, s, list

        def insertAsPred(self, e):
            newNode = self.list.nodeCreator(e, self.pred, self, self.list)
            self.pred.succ = newNode
            self.pred = newNode
            return newNode

        def insertAsSucc(self, e):
            newNode = self.list.nodeCreator(e, self, self.succ, self.list)
            self.succ.pred = newNode
            self.succ = newNode
            return newNode

        def insertNodeAsSucc(self, node):
            node.pred, node.succ  = self, self.succ
            self.succ.pred = node
            self.succ = node
            return node

        def insertNodeAsPred(self, node):
            node.succ, node.pred  = self, self.pred
            self.pred.succ = node
            self.pred = node
            return node

        def isTrailer(self):
            return not self.succ

        def isHeader(self):
            return not self.pred

    def __len__(self):
        return self._size

    def __init__(self, nodeCreator = None, arr=None):
        self.nodeCreator = nodeCreator if nodeCreator else self.Node
        self._header = self.nodeCreator("header", None, None, self)
        self._trailer = self.nodeCreator("trailer", None, None, self)
        self._header.succ = self._trailer
        self._trailer.pred = self._header
        self._size = 0
        self.iter = None
        if arr:
            for i in arr:
                self.insertAsLast(i)

    def __getitem__(self, item):
        if -1 < item < self._size:
            index = 0
            p = self._header.succ
            while index < item:
                p = p.succ
                index += 1
            return p
        return None

    def next(self):
        if not self.iter.succ.succ:
            raise StopIteration
        self.iter = self.iter.succ
        return self.iter

    def __iter__(self):
        self.iter = self._header
        return self

    def header(self):
        return self._header

    def trailer(self):
        return self._trailer

    def isEmpty(self):
        return self._size <= 0

    def first(self):
        return self._header.succ

    def last(self):
        return self._trailer.pred

    def insertAsFirst(self, e):
        self._size += 1
        return self._header.insertAsSucc(e)

    def insertAsLast(self, e):
        self._size += 1
        return self._trailer.insertAsPred(e)

    def insertBeforeP(self, p, e):
        self._size += 1
        return p.insertAsPred(e)

    def insertAfterP(self, p, e):
        self._size += 1
        return p.insertAsSucc(e)

    def insertNodeAfterP(self, p, node):
        if not p == node:
            self._size += 1
            return p.insertNodeAsSucc(node)

    def insertNodeBeforeP(self, p, node):
        if not p == node:
            self._size += 1
            return p.insertNodeAsPred(node)

    def remove(self, p):
        temp = p
        p.pred.succ = p.succ
        p.succ.pred = p.pred
        self._size -= 1
        return temp

    def revers(self):
        if self._size < 2:
            return
        p = self._header
        while p:
            p.pred, p.succ = p.succ, p.pred
            p = p.pred
        self._header, self._trailer = self._trailer, self._header
        self._header.data = "header"
        self._trailer.data = "trailer"

    def find(self, target):
        return self._find(target, self._header, self._size)

    def _find(self, target, p, n):
        "find target in n succ-nodes of p"
        while 0 < n and not p == self._trailer:
            n -= 1
            p = p.succ
            if p.data == target:
                return p
        return None

    def findLast(self, target):
        return self._findfromPred(target, self._trailer, self._size)

    def _findfromPred(self, target, p, n):
        "find target in n pre-nodes of p"
        while 0 < n and not p == self._header:
            n -= 1
            p = p.pred
            if p.data == target:
                return p
        return None

    def search(self, target, p=None, n=-1):
        return self._search(target, p or self._trailer, n if not n == -1 else self._size)

    def _search(self, target, p, n):
        "in ordered list, find node which is less than or equ to target from n succ-nodes of p"
        while 0 <= n and p:
            n -= 1
            p = p.pred
            if p.data <= target:
                break
        return p

    def findPredicate(self, match):
        if not hasattr(match, '__call__'):
            raise Exception('match is not a func')
        p = self._header
        for i in range(self._size):
            p = p.succ
            if match(p):
                return p
        return None

    def getNodeAfterNIndex(self, p, n):
        for i in range(n):
            p = p.succ
        return p

    def max(self, p, n):
        p = p.pred
        maxNode = p
        for i in range(n):
            if maxNode.data < p.data:
                maxNode = p
            p = p.pred
        return maxNode

    def printAll(self):
        p = self.first()
        ret = []
        while p.succ:
            ret.append(p.data)
            p = p.succ
        print ret





if __name__ == '__main__':
    a = DoublyLinkedList()
    a.insertAsFirst(1)
    a.insertAsFirst(2)
    a.insertAsFirst(3)
    a.insertAsFirst(4)
    for i in a:
        print i.data
    a.printAll()
    print a[3].data
    a.revers()
    a.printAll()
    a.insertAsFirst(5)
    print a.search(5).data
    a.printAll()
    print a.max(a._trailer, 5).data





