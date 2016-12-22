import BinTree
import BinNode
import Utils

class BST(BinTree.BinTree):

    def __init__(self):
        BinTree.BinTree.__init__(self)

    def equal(self, binNode, e):
        return not binNode or binNode.data == e

    def search(self, e):
        return self.searchIn(e, self.root())

    def searchIn(self, e, binNode):
        pNode = binNode
        while pNode:
            if self.equal(pNode, e):
                return pNode
            elif e < pNode.data and pNode.LC:
                pNode = pNode.LC
            elif e > pNode.data and pNode.RC:
                pNode = pNode.RC
            else:
                return pNode

    def insert(self, e):
        p = self.search(e)
        if not p:
            ret = self.insertAsRoot(e)
        elif p.data == e:
            return
        elif e < p.data:
            ret = self.insertAsLC(p, e)
        else:
            ret = self.insertAsRC(p, e)
        self.updateHightAbove(ret)
        return ret

    def remove(self, e):
        p = self.search(e)
        if p and p.data == e:
            self.updateHightAbove(self.removeAt(p))
            self._size -= 1

    def removeAt(self, binNode):
        'return binNode parent'
        if binNode.hasLC() and binNode.hasRC():
            succ = binNode.succInOrder()
            retParent = succ.parent
            succ.data, binNode.data = binNode.data, succ.data
            u = succ.parent
            if u == binNode:
                succ = succ.RC
                u.RC = succ
            else:
                succ = succ.RC
                u.LC = succ
            if succ:
                succ.parent = u
        else:
            retParent = binNode.parent
            ch = binNode.LC if binNode.hasLC() else binNode.RC
            if ch:
                ch.parent = binNode.parent
            if binNode.isRoot():
                self._root = ch
            elif binNode.isLC():
                binNode.parent.LC = ch
            else:
                binNode.parent.RC = ch
        return retParent

    def connect34(self, aNode, bNode, cNode, subT1, subT2, subT3, subT4):
        #                 a       b       c
        #          subT1    subT2   subT3   subT4
        aNode.LC = subT1
        if subT1:
            subT1.parent = aNode
        aNode.RC = subT2
        if subT2:
            subT2.parent = aNode
        self.updataHight(aNode)
        cNode.LC = subT3
        if subT3:
            subT3.parent = cNode
        cNode.RC = subT4
        if subT4:
            subT4.parent = cNode
        self.updataHight(cNode)
        bNode.LC = aNode
        aNode.parent = bNode
        bNode.RC = cNode
        cNode.parent = bNode
        return bNode

    def rotateAt(self, v):
        p = v.parent
        g = p.parent
        if p.isLC():    #zig
            if v.isLC():    #zig-zig
                p.parent = g.parent
                return self.connect34(v, p, g, v.LC, v.RC, p.RC, g.RC)
            else:           #zig-zag
                v.parent = g.parent
                return self.connect34(p, v, g, p.LC, v.LC, v.RC, g.RC)
        else:   #zag
            if v.isRC():    #zag-zag
                p.parent = g.parent
                return self.connect34(g, p, v, g.LC, p.LC, v.LC, v.RC)
            else:           #zag-zig
                v.parent = g.parent
                return self.connect34(g, v, p, g.LC, v.LC, v.RC, p.RC)

    def rotateRight(self, binNode):
        if binNode:
            isRoot = binNode.isRoot()
            p = binNode.rotateRight()
            if isRoot:
                self.setRoot(p)
            return p

    def rotateLeft(self, binNode):
        if binNode:
            isRoot = binNode.isRoot()
            p = binNode.rotateLeft()
            if isRoot:
                self.setRoot(p)
            return p

    def maxAt(self, binNode):
        while binNode.RC:
            binNode = binNode.RC
        return binNode

    def max(self):
        return self.maxAt(self._root)

    def minAt(self, binNode):
        while binNode.LC:
            binNode = binNode.LC
        return binNode

    def min(self):
        return self.minAt(self._root)

if __name__ == '__main__':
    #h = input("please input the height of the tree:")
    bt = BST()
    #a = [44, 17, 88, 8, 32, 65, 97, 28, 54, 82, 93, 29, 76, 80]
    a = [6,4,7,2,5,1,3]
    #a = [2,1,6,4,7,3,5]
    for i in a:
        bt.insert(i)
    #bt.printAll()
    print bt.min().data

    p = bt.search(6)
    bt.rotateRight(p)

    #bt._root = bt.search(2).rotateLeft()
    bt.printAll()
    '''
    for i in range (20):
    bt.insert(Utils.randomRange(20))
    node = randomBinNode(bt.root())
    print 'node.data = '+ str(node.data)
    bt.remove(node)
    bt.printAll()
    '''










