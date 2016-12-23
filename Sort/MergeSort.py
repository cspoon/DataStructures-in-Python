import DoublyLinkedList
import Vector


class MergeSort(object):


    def listMergeSort(self, list, p, n):
        "sort n elements at the beginning of node p"
        if n < 2:
            return p
        mid = n / 2
        q = list.getNodeAfterNIndex(p, mid)
        p = self.listMergeSort(list, p, mid)
        q = self.listMergeSort(list, q, n - mid)
        return self.listMerge(list, p, mid, q, n-mid)

    def listMerge(self, list, p, n, q, m):
        pp = p.pred
        while m > 0:
            if n > 0 and p.data <= q.data:
                p = p.succ
                if p == q:
                    break
                n -= 1
            else:
                q = q.succ
                list.insertNodeBeforeP(p, list.remove(q.pred))
                m -= 1
        return pp.succ

    def arrayMergeSort(self, arr, lo, hi):
        if hi - lo < 2:
            return
        mid = (lo + hi) / 2
        self.arrayMergeSort(arr, lo, mid)
        self.arrayMergeSort(arr, mid, hi)
        self.arrayMerge(arr, lo, mid, hi)

    def arrayMerge(self, arr, lo, mid, hi):
        'merge [lo, mi) and [mi, hi)'
        #b = arr[mid:hi]
    
if __name__ == '__main__':
    a = DoublyLinkedList.DoublyLinkedList()
    a.insertAsLast(4)
    a.insertAsLast(3)
    a.insertAsLast(2)
    a.insertAsLast(1)

    a.insertAsLast(6)
    a.insertAsLast(9)
    a.insertAsLast(5)


    a.printAll()

    ms = MergeSort()
    ms.listMergeSort(a, a._header.succ, a.__len__())
    a.printAll()
'''
i.listMergeSort(a)
a.printAll()
print '*' * 20
b = Vector.Vector()
b.append(5)
b.append(7)
b.append(3)
b.append(2)
b.append(1)
b.printAll()
i.arrayMergeSort(b)
b.printAll()
'''
