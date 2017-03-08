import BST
import Utils


class AVL(BST.BST):

    def __init__(self):
        BST.BST.__init__(self)

    def insert(self, e):
        g = BST.BST.insert(self, e)
        while g and not g.isRoot():
            g = g.parent
            if not g.AVLBalanced():
                gType = g.nodeType()
                gParent = g.parent
                rotatedRoot = self.rotateAt(g.tallerChild().tallerChild())
                if gType == Utils.NodeType.Root:
                    self.setRoot(rotatedRoot)
                elif gType == Utils.NodeType.LC:
                    gParent.LC = rotatedRoot
                else:
                    gParent.RC = rotatedRoot
            else:
                self.updataHight(g)
        return g

    def remove(self, e):
        if self.isEmpty():
            raise Utils.Empty('Empty Error~!')
        p = self.search(e)
        if p and p.data == e:
            g = self.removeAt(p)
            self._size -= 1
            while g:
                if not g.AVLBalanced():
                    gType = g.nodeType()
                    gParent = g.parent
                    rotatedRoot = self.rotateAt(g.tallerChild().tallerChild())
                    if gType == Utils.NodeType.Root:
                        self.setRoot(rotatedRoot)
                    elif gType == Utils.NodeType.LC:
                        gParent.LC = rotatedRoot
                    else:
                        gParent.RC = rotatedRoot
                self.updataHight(g)
                g = g.parent
            return True
        return False


if __name__ == '__main__':
    avl = AVL()
    a = [44, 17, 88, 8, 32, 65, 97, 28, 54, 82, 93, 29, 76, 80]
    #a = [8, 6, 9, 4, 7, 3, 5, 10]
    #a = [2, 5]

    for i in a:
        avl.insert(i)
        avl.printAll()
    print ('hehehehe~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    avl.printAll()
    avl.remove(17)
    avl.printAll()

    print('size = ' + avl.size().__str__())
    avl.remove(32)
    print('size = ' + avl.size().__str__())
    avl.printAll()
    print('size = ' + avl.size().__str__())