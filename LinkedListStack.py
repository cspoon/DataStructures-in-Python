import DoublyLinkedList
import Utils


class LinkedListStack(DoublyLinkedList.DoublyLinkedList):

    def push(self, e):
        self.insertAsLast(e)

    def pop(self):
        if self.isEmpty():
            raise Utils.Empty('empty exception')
            ret = self.last()
            self.remove(ret)
            return  ret

    def top(self):
        if self.isEmpty():
            raise Utils.Empty('empty exception')
        return self.last()

if __name__ == '__main__':
    q = LinkedListStack()
    q.push(1)
    q.push(2)
    q.push(5)
    print q.top().data
    q.printAll()

