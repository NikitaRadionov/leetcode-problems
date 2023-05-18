

# FAIL !

class MajorityChecker:

    def __init__(self, a):

        def gen(l, r):

            if l == r - 1:
                node = self.STNode(l, r, {a[l]: 1})
                self.store.append(node)
                return node
            else:
                m = (l + r) // 2
                left_node = gen(l, m)
                right_node = gen(m, r)
                store = {}
                node = self.STNode(l, r, store, left=left_node, right=right_node)
                self.store.append(node)
                return node

        self.store = []
        gen(0, len(a))
        self.root = self.store[len(self.store) - 1]


    def query(self, l: int, r: int, th: int) -> int:

        def find(node, l, r, th):

            l1 = node.l
            r1 = node.r

            m = (l1 + r1) // 2

            if l == l1 and r == r1 - 1:
                 if th <= node.mx:
                     return (node.e, node.mx)
            elif r < m:
                return find(node.left, l, r, th)
            elif l >= m:
                return find(node.right, l, r, th)
            else:
                th1 = th - (r - m + 1) if th - (r - m + 1) > 0 else 1
                th2 = th - (m - l) if th - (m - l) > 0 else 1
                res1 = find(node.left, l, m - 1, th1)
                res2 = find(node.right, m, r, th2)

                if not (res1 is None or res2 is None):

                    e1, mx1 = find(node.left, l, m - 1, th1)
                    e2, mx2 = find(node.right, m, r, th2)
                    mx = max(mx1, mx2)
                    if e1 == e2:
                        mx += 1
                        e = e1
                    else:
                        e = e1 if mx1 > mx2 else e2
                    return (e, mx)


        res = find(self.root, l, r, th)
        if res is None:
            return -1
        else:
            return res[0]

    class STNode:

        def __init__(self, l, r, store={}, left=None, right=None):
            self.l = l
            self.r = r
            self.store = store
            self.left = left
            self.right = right

        def __str__(self):
            return f"( store={self.store}, [{self.l}, {self.r}) )"

        __repr__ = __str__

    def __str__(self):
        return str(self.store)

    __repr__ = __str__




obj = MajorityChecker([1, 1, 2, 2, 1, 1])
print(obj)
print(obj.query(0, 5, 4))
print(obj.query(0, 3, 3))
print(obj.query(2, 3, 2))


from typing import Any

class Dsu:
    """
        This is Disjoin Set Union.
        This implementation uses the heuristic of path compression and pooling by rank
        Complexity of each operation: O(a(n)) a(n) - inverse Ackermann function
        For simplicity, we can assume that we have constant complexity
    """

    def __init__(self):
        self.__storage = {}
        self.__rank = {}


    def make_set(self, x:Any):
        self.__storage[x] = x
        self.__rank[x] = 0


    def find_set(self, x:Any):
        if x == self.__storage[x]:
            return x
        p = self.find_set(self.__storage[x])
        self.__storage[x] = p
        return p


    def have_element(self, x:Any):
        try:
            return self.find_set(x)
        except KeyError:
            return False


    def union_sets(self, a:Any, b:Any):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.__rank[a] < self.__rank[b]:
                c = a
                a = b
                b = c
            self.__storage[b] = a
            if self.__rank[a] == self.__rank[b]:
                self.__rank[a] += 1


    def get_storage(self):
        x = self.__storage.copy()
        return x


    def get_rank(self):
        x = self.__rank.copy()
        return x





# class MajorityChecker:

#     def __init__(self, a):

#         def gen(l, r):

#             if l == r - 1:
#                 node = self.STNode(l, r, 1, a[l])
#                 self.store.append(node)
#                 return node
#             else:
#                 m = (l + r) // 2
#                 left_node = gen(l, m)
#                 right_node = gen(m, r)
#                 mx = max(left_node.mx, right_node.mx)
#                 if left_node.e == right_node.e:
#                     e = left_node.e
#                     mx += 1
#                 else:
#                     e = left_node.e if left_node.mx > right_node.mx else right_node.e
#                 node = self.STNode(l, r, mx, e, left=left_node, right=right_node)
#                 self.store.append(node)
#                 return node

#         self.store = []
#         gen(0, len(a))
#         self.root = self.store[len(self.store) - 1]


#     def query(self, l: int, r: int, th: int) -> int:

#         def find(node, l, r, th):

#             l1 = node.l
#             r1 = node.r

#             m = (l1 + r1) // 2

#             if l == l1 and r == r1 - 1:
#                  if th <= node.mx:
#                      return (node.e, node.mx)
#             elif r < m:
#                 return find(node.left, l, r, th)
#             elif l >= m:
#                 return find(node.right, l, r, th)
#             else:
#                 th1 = th - (r - m + 1) if th - (r - m + 1) > 0 else 1
#                 th2 = th - (m - l) if th - (m - l) > 0 else 1
#                 res1 = find(node.left, l, m - 1, th1)
#                 res2 = find(node.right, m, r, th2)

#                 if not (res1 is None or res2 is None):

#                     e1, mx1 = find(node.left, l, m - 1, th1)
#                     e2, mx2 = find(node.right, m, r, th2)
#                     mx = max(mx1, mx2)
#                     if e1 == e2:
#                         mx += 1
#                         e = e1
#                     else:
#                         e = e1 if mx1 > mx2 else e2
#                     return (e, mx)


#         res = find(self.root, l, r, th)
#         if res is None:
#             return -1
#         else:
#             return res[0]

#     class STNode:

#         def __init__(self, l, r, mx, e, left=None, right=None):
#             self.l = l
#             self.r = r
#             self.mx = mx
#             self.e = e
#             self.left = left
#             self.right = right

#         def __str__(self):
#             return f"( e={self.e}, mx={self.mx}, [{self.l}, {self.r}) )"

#         __repr__ = __str__

#     def __str__(self):
#         return str(self.store)

#     __repr__ = __str__




# obj = MajorityChecker([1, 1, 2, 2, 1, 1])
# print(obj)
# print(obj.query(0, 5, 4))
# print(obj.query(0, 3, 3))
# print(obj.query(2, 3, 2))
