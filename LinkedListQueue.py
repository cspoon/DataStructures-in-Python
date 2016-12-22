import DoublyLinkedList
import Utils


class LinkedListQueue(DoublyLinkedList.DoublyLinkedList):

    def enqueue(self, e):
        self.insertAsLast(e)

    def dequeue(self):
        if self.isEmpty():
            raise Utils.Empty("queue is empty")
        ret = self.first()
        self.remove(ret)
        return ret

if __name__ == '__main__':
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(5)
    print q.dequeue()
    q.printAll()