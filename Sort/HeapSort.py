import Vector
import PriorityQueue


class HeapSort(object):

    def heapSort(self, arr):
        pq = PriorityQueue.PriorityQueue(arr)
        for i in range(pq.__len__()):
            arr[i] = pq.delMax()

if __name__ == '__main__':
    b = Vector.Vector()
    b.append(1)
    b.append(2)
    b.append(3)
    b.append(5)
    b.append(4)
    b.printAll()
    hs = HeapSort()
    hs.heapSort(b)
    b.printAll()