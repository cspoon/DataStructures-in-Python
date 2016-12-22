import Vector
import Utils


class ArrayStack(Vector.Vector):

    def push(self, obj):
        self.append(obj)

    def pop(self):
        if self.isEmpty():
            raise Utils.Empty('empty exception')
        ret = self._elem[self._size - 1]
        self.removeAt(self._size - 1)
        return ret

    def top(self):
        if self.isEmpty():
            raise Utils.Empty('empty exception')
        else:
            return self._elem[self._size - 1]


if __name__ == "__main__":
    a = ArrayStack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.top())
    a.pop()
    print(a.top())
    a.printAll()