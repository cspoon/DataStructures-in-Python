import BinNode
import BST
import Utils


class Color(object):

    Red = 0
    Black = 1


class RBBinNode(BinNode.BinNode):

    def __init__(self, e, p=None, lc=None, rc=None, h=0, color=Color.Black):
        BinNode.BinNode.__init__(e, p, lc, rc, h)
        self.color = color


class LeftLeaningRedBlackTree(BST.BST):

    def __init__(self):
        BST.BST.__init__(self)
        self.printNodeInfo = self.printTreapInfo

    def printTreapInfo(self, node):
        if self.isRed(node):
            print '\033[0;31;m' + str(node.data) + '\033[0m'
        else:
            print node.data

    def isRed(self, node):
        return False if not node else node.color == Color.Red

    def insert(self, e):
        g = BST.BST.insert(self, e)
        g.color = Color.Black if g.isRoot() else Color.Red
        p = g.parent
        while p:
            if self.isRed(p.RC) and not self.isRed(p.LC):
                self.debugPrint('before rotateLeft')
                self.rotateLeft(p)
                self.debugPrint('after rotateLeft')
                self.updataHight(p)
            elif self.isRed(p.LC) and self.isRed(p.LC.LC):
                self.debugPrint('before rotateRight')
                self.rotateRight(p)
                self.updataHight(p)
                self.debugPrint('after rotateRight')
            elif self.isRed(p.LC) and self.isRed(p.RC):
                self.debugPrint('before flipColor')
                self.flipColor(p)
                self.updataHight(p)
                self.debugPrint('after flipColor')
                p = p.parent
            else:
                p = p.parent
                self.updataHight(p)
        if self._root:
            self._root.color = Color.Black

    def rotateLeft(self, binNode):
        BST.BST.rotateLeft(self, binNode)
        if binNode.parent:
            binNode.parent.color = binNode.color
        binNode.color = Color.Red

    def rotateRight(self, binNode):
        BST.BST.rotateRight(self, binNode)
        if binNode.parent:
            binNode.parent.color = binNode.color
        binNode.color = Color.Red

    def flipColor(self, node):
        node.color = Color.Red
        node.LC.color = node.RC.color = Color.Black

if __name__ == '__main__':
    #a = [6, 4, 7, 2, 5, 1, 3, 45, 30, 10, 13, 14, 19, 16]
    b = []
    for i in range(20):
        while True:
            r = Utils.randomRange(1000)
            if not b.__contains__(r):
                b.append(r)
                break
    rbt = LeftLeaningRedBlackTree()
    for i in b:
        rbt.insert(i)
        rbt.printAll()

