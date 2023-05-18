from queue import Queue

def bfs(lst, s):

    q = Queue()
    q.put(s)

    visited, d = {}, {}
    for obj in lst.keys():
        visited[obj] = False
        d[obj] = -1

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


n = int(input())

dots = [None]

for i in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

k = int(input())
a, b = map(int, input().split())

lst = {i: [] for i in range(1, n + 1)}

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if abs(dots[i][0] - dots[j][0]) + abs(dots[i][1] - dots[j][1]) <= k:
            lst[i].append(j)
            lst[j].append(i)

d = bfs(lst, a)
print(d[b])