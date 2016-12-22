import BST
import BinNode


class SplayTree(BST.BST):

    def __init__(self):
        BST.BST.__init__(self)

    def splay(self, v):
        if not v:
            return
        while v.parent and v.parent.parent:
            p = v.parent
            g = p.parent
            #gg = g.parent
            #gType = Utils.NodeType.Root if not g else g.nodeType()
            self.debugPrint('before rotate')
            if p.isLC():                                                                    # g
                if v.isLC():    # zig-zig p and g at same side, rotate g first           p
                    self.rotateRight(self.rotateRight(g))                           # v
                else:   # zig-zag                                                                   g
                    self.rotateLeft(p)                                                      # p
                    self.debugPrint('after Left rotate p')
                    self.rotateRight(g)                                                            # v
                    self.debugPrint('after Right rotate g')
            else:                                                                    # g
                if v.isRC():    # zag-zag p and g at same side, rotate g first            p
                    self.rotateLeft(self.rotateLeft(g))                                     # v
                else:                                                                                   # g
                    self.rotateRight(p)                                                                         # p
                    self.debugPrint('after Right rotate p')
                    self.rotateLeft(g)                                                                       # v
                    self.debugPrint('after Left rotate g')
            '''
                        if gType == Utils.NodeType.Root:
                self.setRoot(v)
            elif gType == Utils.NodeType.LC:
                gg.LC = v
            else:
                gg.RC = v
            '''

            self.updataHight(g)
            self.updataHight(p)
            self.updataHight(v)
        if v.parent:    #break while but v's parent is root, then do a sigle rotate
            p = v.parent
            if v.isLC():
                self.rotateRight(p)
            else:
                self.rotateLeft(p)
            self.updataHight(p)
            self.updataHight(v)
        self.setRoot(v)
        return v

    def insert(self, e):
        if self.isEmpty():
            return self.insertAsRoot(e)
        p = self.search(e)
        if e == p.data:
            return p
        self._size += 1
        oldRoot = self._root
        if self._root.data < e:
            self._root = BinNode.BinNode(e, None, oldRoot, oldRoot.RC)
            oldRoot.parent = self._root
            if oldRoot.hasRC():
                oldRoot.RC.parent = self._root
                oldRoot.RC = None
        else:
            self._root = BinNode.BinNode(e, None, oldRoot.LC, oldRoot)
            oldRoot.parent = self._root
            if oldRoot.hasLC():
                oldRoot.LC.parent = self._root
                oldRoot.LC = None
        self.updateHightAbove(oldRoot)
        return self._root

    def remove(self, e):
        p = self.search(e)
        if not p or not p.data == e:
            return False
        if not self._root.hasLC():
            self.setRoot(self._root.RC)
        elif not self._root.hasRC():
            self.setRoot(self._root.LC)
        else:
            lTree = self._root.LC
            lTree.parent = None
            self._root.LC = None
            self.setRoot(self._root.RC)
            self.search(e)
            self._root.LC = lTree
            lTree.parent = self._root
        return True

    def search(self, e):
        p = self.searchIn(e, self._root)
        if p:
            self.setRoot(self.splay(p))
        return self._root

if __name__ == '__main__':
    #a = [6, 4, 7, 2, 5, 1, 3]
    a = [6, 4]
    st = SplayTree()
    for i in a:
        st.insert(i)
    st.printAll()
    st.insert(7)
    st.printAll()
    st.insert(2)
    st.printAll()
    st.insert(5)
    st.printAll()
    st.insert(1)
    st.printAll()
    st.insert(3)
    st.printAll()
    st.insert(8)
    st.printAll()
    #st.isDebug = True
    st.search(6)
    st.printAll()
    st.remove(6)
    st.printAll()