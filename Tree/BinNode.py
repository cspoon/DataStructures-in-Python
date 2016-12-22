import Utils

class BinNode:

    def __init__(self, e, p=None, lc=None, rc=None, h=0):
        self.data, self.parent, self.LC, self.RC, self.height = e, p, lc, rc, h

    def size(self):
        ret = 1
        if self.LC:
            ret += self.LC.size()
        if self.RC:
            ret += self.RC.size()
        return ret

    @staticmethod
    def stature(x):
        return x.height if x else -1

    def balanceFactor(self):
        return BinNode.stature(self.LC) - BinNode.stature(self.RC)

    def AVLBalanced(self):
        return -2 < self.balanceFactor() < 2

    def insertAsLC(self, e):
        self.LC = BinNode(e, self)

    def insertAsRC(self, e):
        self.RC = BinNode(e, self)

    def hasLC(self):
        return self.LC

    def hasRC(self):
        return self.RC

    def isRoot(self):
        return not self.parent

    def isLC(self):
        return not self.isRoot() and self.parent.LC == self

    def isRC(self):
        return not self.isRoot() and self.parent.RC == self

    def nodeType(self):
        return Utils.NodeType.LC if self.isLC() else (Utils.NodeType.RC if self.isRC() else Utils.NodeType.Root)

    def succInOrder(self):
        'get direct successor by inOrder'
        ret = self
        if self.hasRC():
            ret = self.RC
            while ret.hasLC():
                ret = ret.LC
        else:
            while ret.isRC():
                ret = ret.parent
            ret = ret.parent
        return ret

    def tallerChild(self):
        if BinNode.stature(self.LC) > BinNode.stature(self.RC):
            return self.LC
        elif BinNode.stature(self.LC) < BinNode.stature(self.RC):
            return self.RC
        else:
            return self.LC if self.isLC() else self.RC

    def updateHeight(self):
        self.height = 1 + max(BinNode.stature(self.LC), BinNode.stature(self.RC))
        return self.height

    def rotateRight(self):
        'if self is root needs reset root in caller'
        lc = self.LC
        lc.parent = self.parent
        if lc.parent:
            if self == self.parent.RC:
                self.parent.RC = lc
            else:
                self.parent.LC = lc
        self.LC = lc.RC
        if self.LC:
            self.LC.parent = self
        lc.RC = self
        self.parent = lc
        return lc

    def rotateLeft(self):
        'if self is root needs reset root in caller'
        rc = self.RC
        rc.parent = self.parent
        if rc.parent:
            if self == self.parent.RC:
                self.parent.RC = rc
            else:
                self.parent.LC = rc
        self.RC = rc.LC
        if self.RC:
            self.RC.parent = self
        rc.LC = self
        self.parent = rc
        return rc

    @staticmethod
    def travInRecursive(x, func):
        if not x:
            return
        BinNode.travInRecursive(x.LC, func)
        func(x.data)
        BinNode.travInRecursive(x.RC, func)

    @staticmethod
    def travPreRecursive(x, func):
        if not x:
            return
        func(x.data)
        BinNode.travInRecursive(x.LC, func)
        BinNode.travInRecursive(x.RC, func)

    @staticmethod
    def travPreRecursive(x, func):
        if not x:
            return
        BinNode.travInRecursive(x.LC, func)
        BinNode.travInRecursive(x.RC, func)
        func(x.data)