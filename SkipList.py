import DoublyLinkedList
import Utils
import sys

class SkipList(object):

    class Node(DoublyLinkedList.DoublyLinkedList.Node):
        def __init__(self, e, p, s, list):
            DoublyLinkedList.DoublyLinkedList.Node.__init__(self, e, p, s, list)
            self.above = self.below = None

        def setBelow(self, p):
            self.below = p
            if p:
                p.above = self

    def __init__(self):
        self.lists = [DoublyLinkedList.DoublyLinkedList(self.Node)]
        self._size = 0

    def isEmpty(self):
        return self._size <= 0

    def remove(self, p):
        pass

    def insert(self, e):
        p = self.search(e)
        self._insertAfterP(p, e)
        self._size += 1

    def _insertInAboveLevel(self, e, level, below):
        if level >= self.lists.__len__():
            newlist = DoublyLinkedList.DoublyLinkedList(self.Node)
            self.lists.append(newlist)
            newlist.header().setBelow(self.lists[level-1].header())
            newlist.trailer().setBelow(self.lists[level - 1].trailer())
        slot = self.searchIn(self.lists[level].header(), e)
        newNode = self.lists[level].insertAfterP(slot, e)
        newNode.setBelow(below)
        if Utils.flipCoin():
            self._insertInAboveLevel(e, level + 1, below)

    def _insertAfterP(self, p, e):
        newNode = self.lists[0].insertAfterP(p, e)
        if Utils.flipCoin():
            self._insertInAboveLevel(e, 1, newNode)

    def searchIn(self, p, e):
        while not p.isTrailer() and (p.succ.data <= e):
            p = p.succ
        return p

    def search(self, e):
        if self.isEmpty():
            return self.lists[0].header()
        p = self.lists[self.lists.__len__()-1].header()
        for i in range(self.lists.__len__()):
            p = self.searchIn(p, e)
            if not p.below:
                return p
            p = p.below

    def printAll(self):
        index = self.lists.__len__() - 1
        tempIndex = {}
        for i in range(self.lists[0].__len__()):
            tempIndex[i] = self.lists[0][i]
        for i in range(self.lists.__len__()):
            print 'header',
            currIndex = 0
            for j in range(self.lists[index].__len__()):
                oldIndex = currIndex
                for t in range(currIndex, tempIndex.__len__()):
                    currIndex += 1
                    if tempIndex[t].data == self.lists[index][j].data:
                        break
                count = 2 + (Utils.clamp(currIndex-oldIndex-1, 0, sys.maxint))*8
                print ("-" * count + ">%4s" % str(self.lists[index][j].data)),
            count = 2 + (Utils.clamp(self.lists[0].__len__() - currIndex, 0, sys.maxint)) * 8
            print ("-" * count + ">%4s" % 'trailer')
            index -= 1


if __name__ == '__main__':
    sl = SkipList()

    for i in range(15, 5, -1):
        if i == 11:
            continue
        sl.insert(i)
    sl.printAll()
    '''
    l1 = DoublyLinkedList.DoublyLinkedList(None, [6,7,8,9,10,11,12,13,14,15])
    l2 = DoublyLinkedList.DoublyLinkedList(None, [8,9,11,12])
    l3 = DoublyLinkedList.DoublyLinkedList(None, [8,11])
    l4 = DoublyLinkedList.DoublyLinkedList(None, [11])
    sl.lists.append(l1)
    sl.lists.append(l2)
    sl.lists.append(l3)
    sl.lists.append(l4)
    sl.printAll()
    '''

