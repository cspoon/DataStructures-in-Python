import BST
import Utils

class Treap(BST.BST):

    def __init__(self):
        BST.BST.__init__(self)
        self.priority = {}
        self.printNodeInfo = self.printTreapInfo
        self.testPriority = None
        self.testPriIndex = 0

    def printTreapInfo(self, node):
        print "%s(pr: %s)" % (str(node.data), str(self._getPriority(node)))

    def _treapUp(self, g):
        while g and not g.isRoot():
            if self._getPriority(g) < self._getPriority(g.parent):
                gParent = g.parent
                self.rotateRight(gParent) if g.isLC() else self.rotateLeft(gParent)
                self.updataHight(gParent)
                self.updataHight(g)
            else:
                break
        return g

    def insert(self, e):
        g = BST.BST.insert(self, e)
        self._genRandomPriority(g)
        self._treapUp(g)
        return g

    def remove(self, e):
        pass

    def _getPriority(self, binNode):
        return self.priority[binNode]

    def _genRandomPriority(self, binNode):
        while True:
            if self.testPriority:
                p = self.testPriority[self.testPriIndex]
                self.testPriIndex += 1
            else:
                p = Utils.randomInt(0, 1000)
            if not self.priority.__contains__(p):
                self.priority[binNode] = p
                return p

if __name__ == '__main__':
    a = [6, 4, 7, 2, 5, 1, 3]

    tp = Treap()
    #tp.testPriority = [970, 58, 535, 438, 35, 950, 409]
    for i in a:
        tp.insert(i)
        tp.printAll()

