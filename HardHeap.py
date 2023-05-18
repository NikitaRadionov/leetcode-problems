from typing import Any

class HardHeap:

    def __init__(self, a:list):
        self.store = [self.HNode(i, a[i]) for i in range(len(a))]
        self.build_heap()


    def max_heapify(self, i:int):

        node = self.store[i]
        if node.left < len(self.store) and self.store[node.left].key > node.key:
            largest = node.left
        else:
            largest = i

        if node.right < len(self.store) and self.store[node.right].key > self.store[largest].key:
            largest = node.right

        if largest != i:
            self.store[i].key = self.store[largest].key
            self.store[largest].key = node.key
            self.max_heapify(largest)


    def build_heap(self):
        n = len(self.store)
        for i in range( (n - 2) // 2, -1, -1):
            self.max_heapify(i)


    def add_heapify(self, i:int):
        p = self.store[self.store[i].p]

        if p.i > -1 and i > 0 and p.key < self.store[i].key:
            self.store[p.i].key = self.store[i].key
            self.store[i].key = p.key
            self.add_heapify(p.i)


    def add(self, e:Any):
        n = len(self.store)
        self.store.append(self.HNode(n, e))
        self.add_heapify(n)


    class HNode:

        def __init__(self, i, key):
            self.i = i
            self.key = key
            self.left = 2 * i + 1
            self.right = 2 * (i + 1)
            self.p = (i - 1) // 2

        def __str__(self):
            return str(self.key)

        __repr__ = __str__

    def __str__(self):
        return str(self.store)

    __repr__ = __str__



a = ['a', 'b', 'c', 'd', 'e', 'f']

h = HardHeap(a)
print(h.store[0].key)
h.add('aa')
print(h.store[0].key)
h.add('ab')
print(h.store[0].key)