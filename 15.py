# https://leetcode.com/problems/maximum-sum-of-an-hourglass/submissions/934216897/
# Maximum Sum of an Hourglass

grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]

m = len(grid)
n = len(grid[0])

b = [[0 for j in range(n + 1)] for i in range(m + 1)]

for i in range(m):
    for j in range(n):
        b[i + 1][j + 1] = b[i][j + 1] + b[i + 1][j] - b[i][j] + grid[i][j]

res = 0

for i in range(3, m + 1):
    for j in range(3, n + 1):
        z = b[i][j] - b[i][j - 3] - b[i - 3][j] + b[i - 3][j - 3]
        v = grid[i - 2][j - 3] + grid[i - 2][j - 1]
        res = max(res, z - v)

print(res)
