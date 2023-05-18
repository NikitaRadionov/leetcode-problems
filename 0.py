from queue import Queue
def closestMeetingNode(self, edges:list , node1: int, node2: int) -> int:

    def bfs(lst, s):
        q = Queue()
        q.put(s)
        n = len(lst)
        visited = [False for i in range(n)]
        d = [-1 for i in range(n)]
        visited[s] = True
        d[s] = 0
        while not (q.empty()):
            v = q.get()
            for u in lst[v]:
                if not visited[u]:
                    q.put(u)
                    visited[u] = True
                    d[u] = d[v] + 1
        return d

    def get_listadjacency(edges, n):
        adjlst = [[] for i in range(n + 1)]
        for i in range(len(edges)):
            if edges[i] >= 0:
                adjlst[i].append(edges[i])
        return adjlst

    adj = get_listadjacency(edges, len(edges))
    d1 = bfs(adj, node1)
    d2 = bfs(adj, node2)
    m = 1.8446744e+19
    node = -1
    for i in range(len(d1)):
        if d1[i] >= 0 and d2[i] >= 0:
            now = max(d1[i], d2[i])
            if now < m:
                m = now
                node = i

    return node


edges = [5,4,5,4,3,6,-1]
node1 = 0
node2 = 1
print(closestMeetingNode(edges, node1, node2))