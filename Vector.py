import ctypes


class Vector(object):

    def __init__(self):
        self._defaultCapacity = 4
        self._size = 0
        self._capacity = self._defaultCapacity
        self._elem = self._make_array(self._capacity)

    def __getitem__(self, k):
        return self._elem[k]

    def __setitem__(self, key, value):
        self._elem[key] = value

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size <= 0

    def _expand(self):
        if self._size < self._capacity:
            return
        if self._capacity < self._defaultCapacity:
            self._capacity = self._defaultCapacity
        self._resize(2 * self._capacity)

    def insert(self, rank, obj):
        if rank < 0 or rank > self._size:
            raise IndexError('invalid index')
        self._expand()
        for i in range(self._size, rank, -1):
            self._elem[i] = self._elem[i-1]
        self._elem[rank] = obj
        self._size += 1
        return rank

    def append(self, obj):
        return self.insert(self._size, obj)

    def _resize(self, c):
        temp = self._make_array(c)
        for k in range(self._size):
            temp[k] = self._elem[k]
        self._elem = temp
        self._capacity = c

    def traverse(self, fun):
        if hasattr(fun, '__call__'):
            for i in range(0, self._size):
                fun(self._elem[i])

    def removeRange(self, low, high):
        'remove range: [low, high)'
        if low < 0 or high > self._size:
            raise IndexError('invalid index')
        if low == high: return
        if low > high:
            low, high = high, low
        while high < self._size:
            self._elem[low] = self._elem[high]
            low += 1
            high += 1
        for i in range(low, self._size):
            self._elem[i] = None
        self._size = low

    def removeAt(self, index):
        self.removeRange(index, index+1)

    def reverse(self):
        self._reverse(0, self._size-1)

    def _reverse(self, low, high):
        while low < high:
            self._elem[low], self._elem[high] = self._elem[high], self._elem[low]
            low += 1
            high -= 1

    def printAll(self):
        print self._elem[0:self._size]

    def _make_array(self, c):
        return (c*ctypes.py_object)()

    def search(self, e, lo=-1, hi=-1):
        lo = lo if not lo == -1 else 0
        hi = hi if not hi == -1 else self._size
        return self.binSearch(e, lo, hi)

    def binSearch(self, e, lo, hi):
        '[lo, hi)'
        while(lo < hi):
            mid = (lo + hi) / 2
            if e < self._elem[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo-1

    def maxIndex(self, lo, high):
        'find max index in [low, high)'
        high -= 1
        maxIndex = high
        while lo < high:
            high -= 1
            if self._elem[maxIndex] < self._elem[high]:
                maxIndex = high
        return maxIndex

if __name__ == "__main__":
    a = Vector()
    a.append(1)
    a.append(2)
    a.append(4)
    #a.append(4)
    #a.append(6)
    a.printAll()
    print a.search(2, 0, 1)
    a.insert(a.search(3)+1, 3)
    a.printAll()
    print a.maxIndex(0, 1)
    #a.reverse()
    #a.printAll()
    '''
    a.removeRange(3, 0)
    a.printAll()
    a.removeAt(1)
    a.printAll()
    '''








