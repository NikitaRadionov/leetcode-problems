class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = [TreeNode(5), TreeNode(1), TreeNode(4), None, None, TreeNode(3), TreeNode(6)]
root = [TreeNode(2), TreeNode(1), TreeNode(3)]


def isValid(root):
    n = len(root)
    for i in range(n):
        if root[i] is None:
            if 2*i + 1 < n:
                if not root[2*i + 1] is None:
                    return False
            if 2*(i + 1) < n:
                if not root[2*(i + 1)] is None:
                    return False
        else:
            if 2*i + 1 < n:
                if (not (root[2*i + 1] is None)) and root[2*i + 1].val > root[i].val:
                    return False

            if 2*(i + 1) < n:
                if (not (root[2*(i + 1)] is None)) and root[2*(i + 1)].val < root[i].val:
                    return False
    return True

print(isValid(root))