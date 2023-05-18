n = 19
f = [-1, 1, 2] + [0 for _ in range(n - 2)]
for k in range(3,n + 1):
    f[k] = 2 * f[k - 1]
    for i in range(2, k):
        f[k] += f[i - 1] * f[k - i]
print(f)
print(f[n])
