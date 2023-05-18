from typing import Optional, List, Any
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        store = []

        q = Queue()
        q.put((root, 0, 1))

        while not (q.empty()):
            v, dpth, order = q.get()
            if not (v is None):
                if dpth == len(store):
                    store.append([v.val])
                else:
                    if order:
                        store[dpth].append(v.val)
                    else:
                        store[dpth] = [v.val] + store[dpth]
                if not (v.left is None):
                    q.put((v.left, dpth + 1, not order))
                if not (v.right is None):
                    q.put((v.right, dpth + 1, not order))

        return store


# root = TreeNode(val=3)
# node1 = TreeNode(val=9)
# node2 = TreeNode(val=20)
# node3 = TreeNode(val=15)
# node4 = TreeNode(val=7)

# root.left = node1
# root.right = node2
# node2.left = node3
# node2.right = node4



root = TreeNode(val=1)
node1 = TreeNode(val=2)
node2 = TreeNode(val=3)
node3 = TreeNode(val=4)
node4 = TreeNode(val=5)

root.left = node1
root.right = node2
node1.left = node3
node2.right = node4

print(Solution().zigzagLevelOrder(root))



# print(not 0)
# print(not 1)

# if 1:
#     print(1)
# else:
#     0

# if 0:
#     print(0)
# else:
#     print(1)



# def graph_bfs(lst:list | dict, s:Any, weight:bool = False) -> tuple:

#     q = Queue()
#     q.put(s)

#     visited, p, d = {}, {}, {}
#     for obj in lst.keys():
#         visited[obj] = False
#         p[obj] = None
#         d[obj] = -1

#     visited[s] = True
#     d[s] = 0

#     while not (q.empty()):
#         v = q.get()
#         for u in lst[v]:
#             if not visited[u]:
#                 q.put(u)
#                 visited[u] = True
#                 d[u] = d[v] + 1
#                 p[u] = v

#     return (visited, d, p)