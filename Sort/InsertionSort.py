import DoublyLinkedList
import Vector


class InsertionSort(object):

    def listInsertionSort(self, list):
        p = list.first()
        for i in range(list.__len__()):
            pSucc = p.succ
            list.insertNodeAfterP(list.search(p.data, p, i), list.remove(p))
            p = pSucc
            '''
            list.insertAfterP(list.search(p.data, p, i), p.data)
            p = p.succ
            list.remove(p.pred)
            '''

    def arrayInsertionSort(self, arr):
        for i in range(1, arr.__len__()):
            e = arr[i]
            index = arr.search(e,0,i)
            if not arr[index] == e:
                arr.removeAt(i)
                arr.insert(index+1, e)
            '''
            e = arr[i]
            arr.removeAt(i)
            arr.insert(arr.search(e, 0, i)+1, e)
            '''




if __name__ == '__main__':
    a = DoublyLinkedList.DoublyLinkedList()
    a.insertAsFirst(1)
    a.insertAsFirst(2)
    a.insertAsFirst(3)
    a.insertAsFirst(7)
    a.insertAsFirst(5)
    a.printAll()
    i = InsertionSort()
    i.listInsertionSort(a)
    a.printAll()
    print '*' * 20
    b = Vector.Vector()
    b.append(1)
    b.append(2)
    b.append(3)
    b.append(5)
    b.append(4)
    b.printAll()
    i.arrayInsertionSort(b)
    b.printAll()