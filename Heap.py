

# Если нужно получать максимум после очередного доавбления за O(log(n)), то используй это:
class Heap:

    def __init__(self, a:list):
        self.store = a.copy()
        self.build_heap()

    def max_heapify(self, i:int):

        left = 2 * i + 1
        right = 2 * (i + 1)

        if left < len(self.store) and self.store[left] > self.store[i]:
            largest = left
        else:
            largest = i

        if right < len(self.store) and self.store[right] > self.store[largest]:
            largest = right

        if i != largest:
            c = self.store[i]
            self.store[i] = self.store[largest]
            self.store[largest] = c
            self.max_heapify(largest)

    def add_heapify(self, i:int):
        p = (i - 1) // 2
        if i > 0 and self.store[i] > self.store[p]:
            c = self.store[p]
            self.store[p] = self.store[i]
            self.store[i] = self.store[p]
            self.add_heapify(p)

    def add(self, e:int):
        n = len(self.store)
        self.store.append(e)
        self.add_heapify(n)

    def build_heap(self):
        n = len(self.store)
        for i in range((n - 2) // 2, -1, -1):
            self.max_heapify(i)

    @property
    def maximum(self):
        return self.store[0]

    def __str__(self):
        return str(self.store)

    __repr__ = __str__







# a = [1, 2, 3, 4, 5, 6]
# h = Heap(a)
# print(h.maximum)
# h.add(14)
# h.add(7)
# print(h.maximum)
# h.add(20)
# print(h.maximum)


# Если нужно получать минимум после очередного добавления, то можно использовать вот это:


from queue import PriorityQueue


q = PriorityQueue()

q.put((1, "A"))
q.put((3, "B"))
q.put((2, "C"))

c = q.get()

print(type(c))


# Или можно использовать вот это, если модули запрещены:

class MinHeap:

    def __init__(self, a:list):
        self.store = a.copy()
        self.build_heap()

    def min_heapify(self, i:int):

        left = 2 * i + 1
        right = 2 * (i + 1)

        if left < len(self.store) and self.store[left] < self.store[i]:
            largest = left
        else:
            largest = i

        if right < len(self.store) and self.store[right] < self.store[largest]:
            largest = right

        if i != largest:
            c = self.store[i]
            self.store[i] = self.store[largest]
            self.store[largest] = c
            self.min_heapify(largest)

    def add_heapify(self, i:int):
        p = (i - 1) // 2
        if i > 0 and self.store[i] < self.store[p]:
            c = self.store[p]
            self.store[p] = self.store[i]
            self.store[i] = self.store[p]
            self.add_heapify(p)

    def add(self, e:int):
        n = len(self.store)
        self.store.append(e)
        self.add_heapify(n)

    def build_heap(self):
        n = len(self.store)
        for i in range((n - 2) // 2, -1, -1):
            self.min_heapify(i)

    @property
    def minimum(self):
        return self.store[0]

    def __str__(self):
        return str(self.store)

    __repr__ = __str__



a = [1, 2, 3, 4, 5, 6]
h = MinHeap(a)
print(h.minimum)
h.add(14)
h.add(7)
print(h.minimum)
h.add(-1)
print(h.minimum)
