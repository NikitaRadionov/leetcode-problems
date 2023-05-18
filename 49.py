from typing import List

class NumArray:

    def __init__(self, nums: List[int]):

        def gen(l, r):
            if l == r - 1:
                node = self.STNode(l, r, nums[l])
                self.store.append(node)
                return node
            else:
                m = (l + r) // 2
                left_node = gen(l, m)
                right_node = gen(m, r)
                s = left_node.value + right_node.value
                node = self.STNode(l, r, s, left=left_node, right=right_node)
                self.store.append(node)
                return node


        self.store = []
        self.root = gen(0, len(nums))


    def update(self, index: int, val: int) -> None:

        def walk(node, index):
            l = node.l
            r = node.r
            m = (l + r) // 2
            if r - 1 == l and l == index:
                node.value = val
                return node
            elif index < m:
                updated_node = walk(node.left, index)
                node.value = updated_node.value + node.right.value
                return node
            elif index >= m:
                updated_node = walk(node.right, index)
                node.value = updated_node.value + node.left.value
                return node

        walk(self.root, index)


    def sumRange(self, left: int, right: int) -> int:

        def find(node, left, right):
            l = node.l
            r = node.r
            m = (l + r) // 2
            if l == left and r - 1 == right:
                return node.value
            elif right < m:
                return find(node.left, left, right)
            elif left >= m:
                return find(node.right, left, right)
            else:
                s1 = find(node.left, left, m - 1)
                s2 = find(node.right, m, right)
                return s1 + s2

        return find(self.root, left, right)


    class STNode:

        def __init__(self, l, r, value, left=None, right=None):
            self.l = l
            self.r = r
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            return str((self.l, self.value, self.r))

        __repr__ = __str__

    def __str__(self):
        return str(self.store) + "\n" + str(self.root)

    __repr__ = __str__


tree = NumArray([1, 3, 5])
print(tree.sumRange(0, 2))
print(tree.update(1, 2))
print(tree.sumRange(0, 2))


# tree = NumArray([-2, 0, 3, -5, 2, -1])
# print(tree)
# print(tree.sumRange(0, 2))
# print(tree.sumRange(2, 5))
# print(tree.sumRange(0, 5))



# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.b = [0]
#         for i in range(len(nums)):
#             self.b.append(self.b[i] + nums[i])

#     def sumRange(self, left: int, right: int) -> int:
#         return self.b[right + 1] - self.b[left]


# obj = NumArray([-2, 0, 3, -5, 2, -1])
# print(obj.sumRange(0, 2))
# print(obj.sumRange(2, 5))
# print(obj.sumRange(0, 5))