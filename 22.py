class BinNode:

    def __init__(self, key, left=None, right=None, p=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p

    def __str__(self):
        return str((self.left if self.left is None else self.left.key,
                    self.key,
                    self.right if self.right is None else self.right.key
                    ))

    __repr__ = __str__


def insert(root, node):
    if node.key > root.key:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def search(root, key):
    if key > root.key:
        if root.right is None:
            return False
        else:
            return search(root.right, key)

    if key < root.key:
        if root.left is None:
            return False
        else:
            return search(root.left, key)

    if key == root.key:
        return True


def create_tree(tree):
    n = len(tree)
    root = tree[0]
    for i in range(1, n):
        insert(root, tree[i])


def walk(node):
    if not (node.left is None):
        walk(node.left)
    print(node.key)
    if not (node.right is None):
        walk(node.right)



tree = [BinNode(8),
        BinNode(3), BinNode(10),
        BinNode(1), BinNode(6), BinNode(9), BinNode(14),
        BinNode(4), BinNode(7), BinNode(12), BinNode(16),
        BinNode(11), BinNode(13), BinNode(18), BinNode(20)]



if __name__ == "__main__":
    create_tree(tree)
    print(search(tree[0], 15))
    print(search(tree[0], 14))
