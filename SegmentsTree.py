class SegmentsTree:


    def __init__(self, a:list):


        def gen(l1, r1):

            if l1 == r1 - 1:
                s = a[l1]
                node = self.STNode(s, l1, r1)
                self.b.append(node)
                return (s, node)
            else:
                r2, l2 = (l1 + r1) // 2, (l1 + r1) // 2
                left_s, left_node = gen(l1, r2)
                right_s, right_node = gen(l2, r1)
                s = left_s + right_s
                node = self.STNode(s, l1, r1, left=left_node, right=right_node)
                self.b.append(node)
                return (s, node)

        self.b = []
        gen(0, len(a))
        self.root = self.b[len(self.b) - 1]


    class STNode:

        def __init__(self, s, l, r, left=None, right=None):
            self.s = s
            self.l = l
            self.r = r
            self.left = left
            self.right = right


        def __str__(self):
            return f"( [{self.l}, {self.r}), {self.s} )"

        __repr__ = __str__


    def summ_request(self, l, r):

        def find(node, l, r):

            l1 = node.l
            r1 = node.r

            m = (l1 + r1) //2

            if l == l1 and r == r1 - 1:
                return node.s
            elif r < m:
                s = find(node.left, l, r)
                return s
            elif l >= m:
                s = find(node.right, l, r)
                return s
            else:
                s1 = find(node.left, l, m - 1)
                s2 = find(node.right, m, r)
                return s1 + s2

        s = find(self.root, l, r)
        return s


    def update_request(self, i, x):

        def update(node, i, x):

            l1 = node.l
            r1 = node.r

            m = (l1 + r1) // 2

            if i < m:
                left_s = update(node.left, i, x)
                node.s = left_s + node.right.s
                return node.s
            elif r1 - 1 > l1:
                right_s = update(node.right, i, x)
                node.s = node.left.s + right_s
                return node.s
            else:
                node.s = x
                return node.s

        update(self.root, i, x)
        print("OK")


    def __str__(self):
        return str(self.root)

    __repr__ = __str__



a = [4, 5, 1, 8, 10, 52, 32, 80, 61, 39, 91, -5, -9, -1, 0, 3, 10, 15, 18]

tree = SegmentsTree(a)
prev = tree.summ_request(0, 5)
print(prev)
tree.update_request(2, 3)
nxt = tree.summ_request(0, 5)
print(nxt)
print(nxt - prev)