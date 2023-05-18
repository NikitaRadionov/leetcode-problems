from queue import PriorityQueue


q = PriorityQueue()

q.put((1, "A"))
q.put((3, "B"))
q.put((2, "C"))

c = q.get()

print(type(c))