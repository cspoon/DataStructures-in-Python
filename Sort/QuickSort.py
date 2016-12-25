import Vector
import DoublyLinkedList
import Utils

class QuickSort(object):

    def arrQuickSort(self, arr, lo, hi):
        if hi - lo < 2:
            return
        mid = self.arrPatition(arr, lo, hi)
        self.arrQuickSort(arr, lo, mid)
        self.arrQuickSort(arr, mid+1, hi)

    def arrPatition(self, arr, lo, hi):
        '[lo, hi]'
        randInt = Utils.randomRange(hi -lo - 1)
        arr[lo], arr[lo + randInt] = arr[lo + randInt], arr[lo]
        pivot = arr[lo]
        while lo < hi:
            while lo < hi and pivot <= arr[hi]:
                hi -= 1
            arr[lo] = arr[hi]
            while lo < hi and arr[lo] <= pivot:
                lo += 1
            arr[hi] = arr[lo]
        arr[lo] = pivot
        return  lo

    def listQuickSort(self, list):
        pass

if __name__ == '__main__':
    i = QuickSort()
    '''
    a = DoublyLinkedList.DoublyLinkedList()
    a.insertAsFirst(1)
    a.insertAsFirst(2)
    a.insertAsFirst(3)
    a.insertAsFirst(7)
    a.insertAsFirst(5)
    a.printAll()
    i.listQuickSort(a)
    a.printAll()
    '''

    print '*' * 20
    b = Vector.Vector()
    b.append(5)
    b.append(7)
    b.append(3)
    b.append(2)
    b.append(1)
    b.printAll()
    i.arrQuickSort(b, 0, b.__len__()-1)
    b.printAll()