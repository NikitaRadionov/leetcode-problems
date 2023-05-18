class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def walk(root):
            left = not root.left is None
            right = not root.right is None

            if left and (not right):
                mx, mn, b = walk(root.left)
                b = not (mx >= root.val or (not b))
                b = b and (root.left.val < root.val)
                mx = max(mx, root.val, mn)
                mn = min(mx, root.val, mn)
                return (mx, mn, b)

            if right and (not left):
                mx, mn, b = walk(root.right)
                b = not (mn <= root.val or (not b))
                b = b and (root.val < root.right.val)
                mx = max(mx, root.val, mn)
                mn = min(mx, root.val, mn)
                return (mx, mn, b)

            if left and right:
                mx1, mn1, b1 = walk(root.left)
                mx2, mn2, b2 = walk(root.right)
                b =  mx1 < root.val < mn2 and b1 and b2
                b = b and (root.left.val < root.val < root.right.val)
                mx = max(mx1, mn1, root.val, mx2, mn2)
                mn = min(mx1, mn1, root.val, mx2, mn2)
                return (mx, mn, b)

            if not (left or right):
                mx, mn = root.val, root.val
                return (mx, mn, True)

        res = walk(root)[2]
        return res
