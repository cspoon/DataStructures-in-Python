import BinTree
import Utils

def randomBinTree(bt, x, h):
    if h <= 0:
        return
    if Utils.randomRange(h):
        randomBinTree(bt, bt.insertAsRC(x, Utils.randomRange(100)), h - 1)
    if Utils.randomRange(h):
        randomBinTree(bt, bt.insertAsLC(x, Utils.randomRange(100)), h - 1)

def randomBinNode(binNode):
    if (not binNode.hasLC()) and (not binNode.hasRC()):
        return binNode
    elif not binNode.hasLC():
        return Utils.randomRange(1) and randomBinNode(binNode.RC) or binNode
    elif not binNode.hasRC():
        return Utils.randomRange(1) and randomBinNode(binNode.LC) or binNode
    else:
        return Utils.randomRange(1) and  randomBinNode(binNode.LC) or randomBinNode(binNode.RC)

def randomCompleteBinTree(bt, x, h, isOrder):
    if h <= 0:
        return
    randomCompleteBinTree(bt, bt.insertAsLC(x, isOrder and x.data*2+1 or Utils.randomRange(100)), h - 1, isOrder)
    randomCompleteBinTree(bt, bt.insertAsRC(x, isOrder and x.data*2+2 or Utils.randomRange(100)), h - 1, isOrder)

if __name__ == '__main__':
    #h = input("please input the height of the tree:")
    bt = BinTree.BinTree()
    bt.insertAsRoot(0)
    randomCompleteBinTree(bt, bt.root(), 3, True)
    bt.printAll()
    '''
    node = randomBinNode(bt.root())
    print 'node.data = '+ str(node.data)
    bt.remove(node)
    bt.printAll()
    '''

