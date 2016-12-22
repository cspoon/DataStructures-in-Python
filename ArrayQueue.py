import Vector
import Utils


class ArrayQueue(Vector.Vector):

    def __init__(self):
        Vector.Vector.__init__(self)
        self._front = 0

    def first(self):
        if self.isEmpty():
            raise Utils.Empty('queue is empty')
        return self._elem[self._front]

    def enqueue(self, e):
        self._expand()
        tail = (self._front + self._size) % self._capacity
        self._elem[tail] = e
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Utils.Empty("queue is empty")
        ret = self.first()
        self._elem[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return ret

    def _resize(self, c):
        temp = self._make_array(c)
        walk = self._front
        for k in range(self._size):
            temp[k] = self._elem[walk]
            walk = (walk+1) % self._capacity
        self._elem = temp
        self._front = 0
        self._capacity = c

    def printAll(self):
        walk = self._front
        ret = []
        for k in range(self._size):
            ret.append(self._elem[walk])
            walk = (walk + 1) % self._capacity
        print ret

if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.printAll()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(5)
    q.enqueue(6)

    q.printAll()



