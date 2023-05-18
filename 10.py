a = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, -36]
]

n = len(a)
m = len(a[0])
d = [[0 for j in range(m + 1)] for i in range(n)]
b = [[0 for j in range(m + 1)] for i in range(n + 1)]


for i in range(n):
    for j in range(1, m + 1):
        d[i][j] = d[i][j - 1] + a[i][j - 1]

for j in range(1, m + 1):
    for i in range(1, n + 1):
        b[i][j] = b[i - 1][j] + d[i - 1][j]

for i in range(n + 1):
    print(b[i])
