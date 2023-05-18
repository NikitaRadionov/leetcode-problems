from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    __repr__ = __str__

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.mx = -1001
        def walk(node):
            if node is None:
                return 0

            left_mx = max(walk(node.left), 0)
            right_mx = max(walk(node.right), 0)

            self.mx = max(node.val + left_mx + right_mx, self.mx)
            return max(left_mx, right_mx) + node.val

        walk(root)
        return self.mx



root = TreeNode(-10)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# root.left = node1
# root.right = node2

# root = TreeNode(-3)

print(Solution().maxPathSum(root))




# Brute force O(n^2)
# class Solution:

#     def maxPathSum(self, root: Optional[TreeNode]) -> int:

#         def create_lstadj(node):
#             if not (node is None):

#                 if not (node.left is None):
#                     lstadj[node].append(node.left)
#                     if not (node.left in lstadj.keys()):
#                         lstadj[node.left] = [node]
#                     create_lstadj(node.left)


#                 if not (node.right is None):
#                     lstadj[node].append(node.right)
#                     if not (node.right in lstadj.keys()):
#                         lstadj[node.right] = [node]
#                     create_lstadj(node.right)


#         def compute_tree(node):

#             dp = []
#             visited = {n: 0 for n in lstadj.keys()}

#             def walk(node, val):
#                 visited[node] = 1
#                 val += node.val
#                 dp.append(val)
#                 for nxt in lstadj[node]:
#                     if not visited[nxt]:
#                         walk(nxt, val)

#             walk(node, 0)

#             now_mx = max(dp)
#             return now_mx

#         lstadj = {root: []}
#         create_lstadj(root)
#         mx_g = -1001
#         for node in lstadj.keys():
#             now_mx = compute_tree(node)
#             if now_mx > mx_g:
#                 mx_g = now_mx
#         return mx_g


# Жадный алгоритм (не работает)

# class Solution:

#     def maxPathSum(self, root: Optional[TreeNode]) -> int:

#         def create_lstadj(node):
#             if not (node is None):

#                 if not (node.left is None):
#                     lstadj[node].append(node.left)
#                     if not (node.left in lstadj.keys()):
#                         lstadj[node.left] = [node]
#                     create_lstadj(node.left)


#                 if not (node.right is None):
#                     lstadj[node].append(node.right)
#                     if not (node.right in lstadj.keys()):
#                         lstadj[node.right] = [node]
#                     create_lstadj(node.right)

#         def walk(node):
#             visited[node] = 1
#             summ[0] += node.val
#             if mx[0] < summ[0]:
#                 mx[0] = summ[0]
#             next_node = None
#             next_mx = -1001
#             for nxt in lstadj[node]:
#                 if not visited[nxt] and nxt.val > next_mx:
#                     next_node = nxt
#                     next_mx = nxt.val
#             if not (next_node is None):
#                 walk(next_node)

#         lstadj = {root: []}
#         create_lstadj(root)
#         mx_g = -1001
#         for node in lstadj.keys():
#             visited = {node: 0 for node in lstadj.keys()}
#             mx = [-1001]
#             summ = [0]
#             walk(node)
#             if mx[0] > mx_g:
#                 mx_g = mx[0]
#         return mx_g
