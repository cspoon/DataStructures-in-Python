#vim: set fileencoding:utf-8
import BinNode
import Utils

class BinTree:

    def __init__(self):
        self._size = 0
        self._root = None
        self.isDebug = False
        self.printNodeInfo = None

    def size(self):
        return self._size

    def root(self):
        return self._root

    def setRoot(self, root):
        self._root = root
        if self._root:
            root.parent = None


    def isEmpty(self):
        return not self._root

    @staticmethod
    def updataHight(x):
        if not x:
            return
        x.height = 1 + max(BinNode.BinNode.stature(x.LC), BinNode.BinNode.stature(x.RC))
        return x.height

    @staticmethod
    def updateHightAbove(x):
        "update hight of x's ancestors"
        while x:
            BinTree.updataHight(x)
            x = x.parent

    def insertAsRoot(self, e):
        self._size = 1
        self._root = BinNode.BinNode(e)
        return self._root

    def insertAsLC(self, x, e):
        self._size += 1
        x.insertAsLC(e)
        BinTree.updateHightAbove(x)
        return x.LC

    def insertAsRC(self, x, e):
        self._size += 1
        x.insertAsRC(e)
        BinTree.updateHightAbove(x)
        return x.RC

    def attachAsLC(self, x, subTree):
        if not subTree or not subTree.root():
            return
        x.LC = subTree.root()
        x.LC.parent = x
        self._size += subTree.size
        BinTree.updateHightAbove(x)
        subTree._root = None
        subTree._size = 0
        return x

    def attachAsRC(self, x, subTree):
        if not subTree or not subTree.root():
            return
        x.RC = subTree.root()
        x.RC.parent = x
        self._size += subTree.size
        BinTree.updateHightAbove(x)
        subTree._root = None
        subTree._size = 0
        return x

    def removeSubTree(self, binNode):
        if binNode.isRoot():
            self._root = None
        elif binNode.isLC():
            binNode.parent.LC = None
        else:
            binNode.parent.RC = None
        self.updateHightAbove(binNode.parent)
        ret = self.removeAt(binNode)
        self._size -= ret
        return ret

    def removeAt(self, bindNode):
        if not bindNode:
            return 0
        ret = 1 + self.removeAt(bindNode.LC) + self.removeAt(bindNode.RC)
        bindNode.data = None
        return ret

    def printAll(self):
        print ("****************** tree's size == %s ******************" % str(self._size))
        self.printTree(self._root, 0, Utils.NodeType.Root, {})

    def printTree(self, node, depth, type, bTypes):
        if not node:
            return
        bTypes[depth] = type
        self.printTree(node.RC, depth + 1, Utils.NodeType.RC, bTypes)
        print "%-20s" % str(node.data),
        for i in range(depth):
            if bTypes[i] + bTypes[i + 1]:
                print "      ",
            else:
                print "│    ",
        if type == Utils.NodeType.RC:
            print "┌──",
        elif type == Utils.NodeType.LC:
            print "└──",
        else:
            "──",
        #print "%s(p=%s)" % (str(node.data), str(node.parent.data if node.parent else 'r'))
        if self.printNodeInfo:
            self.printNodeInfo(node)
        else:
            print node.data
        self.printTree(node.LC, depth + 1, Utils.NodeType.LC, bTypes)

    def debugPrint(self, str):
        if self.isDebug:
            print str
            self.printAll()



