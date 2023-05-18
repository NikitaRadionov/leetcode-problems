from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not (node is None):
                if depth > mx[0]:
                    mx[0] = depth
                if not (node.left is None):
                    dfs(node.left, depth + 1)
                if not (node.right is None):
                    dfs(node.right, depth + 1)

        mx = [0]
        dfs(root, 1)
        return mx[0]


root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

print(Solution().maxDepth(root))