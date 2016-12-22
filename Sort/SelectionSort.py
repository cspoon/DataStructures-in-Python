import DoublyLinkedList
import Vector


class SelectionSort(object):

    def listSelectionSort(self, list):
        trailer = list._trailer
        for i in range(list.__len__(), 1, -1):
            max = list.max(trailer, i)
            list.insertNodeAfterP(trailer.pred, list.remove(max))
            trailer = trailer.pred


    def arraySelectionSort(self, arr):
        for i in range(arr.__len__(), 1, -1):
            maxIndex = arr.maxIndex(0, i)
            arr[maxIndex], arr[i-1] = arr[i-1], arr[maxIndex]

if __name__ == '__main__':
    a = DoublyLinkedList.DoublyLinkedList()
    a.insertAsFirst(1)
    a.insertAsFirst(2)
    a.insertAsFirst(3)
    a.insertAsFirst(7)
    a.insertAsFirst(5)
    a.printAll()
    i = SelectionSort()
    i.listSelectionSort(a)
    a.printAll()
    print '*' * 20
    b = Vector.Vector()
    b.append(5)
    b.append(7)
    b.append(3)
    b.append(2)
    b.append(1)
    b.printAll()
    i.arraySelectionSort(b)
    b.printAll()
