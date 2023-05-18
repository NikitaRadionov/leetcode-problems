grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

n = len(grid)
m = len(grid[0])
dp = [[grid[0][0]] + [0 for _ in range(m - 1)]] + [[0 for _ in range(m)] for i in range(n - 1)]

i = 1

while i < max(n, m):

    if i < m:
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    if i < n:
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    i += 1

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

print(dp[n - 1][m - 1])