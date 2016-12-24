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
        b = arr[lo:mid]
        lb, lc = mid - lo, hi - mid
        pb = pa = pc = 0
        while pb < lb or pc < lc:
            if pb < lb and (pc >= lc or b[pb] <= arr[mid+pc]):
                arr[lo+pa] = b[pb]
                pb += 1
            elif pc < lc and (pb >= lb or arr[mid+pc] < b[pb]):
                arr[lo+pa] = arr[mid+pc]
                pc += 1
            pa += 1


if __name__ == '__main__':
    a = DoublyLinkedList.DoublyLinkedList()
    ms = MergeSort()
    '''
    a.insertAsLast(4)
    a.insertAsLast(3)
    a.insertAsLast(2)
    a.insertAsLast(1)
    a.insertAsLast(6)
    a.insertAsLast(9)
    a.insertAsLast(5)
    a.printAll()
    ms.listMergeSort(a, a._header.succ, a.__len__())
    a.printAll()
    print '*' * 20
    '''

    b = Vector.Vector()
    b.append(1)
    b.append(4)
    b.append(3)
    b.append(9)
    b.append(11)
    b.append(6)
    b.append(2)
    b.printAll()
    ms.arrayMergeSort(b, 0,b.__len__())
    b.printAll()

