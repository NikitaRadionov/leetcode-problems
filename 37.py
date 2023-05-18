# n = 5

# dp = [0, 1, 1] + [0 for _ in range(n - 2)]

# for i in range(3, n + 1):
#     s = set()
#     for j in range(1, int(i ** 0.5) + 1):
#         if i % j == 0:
#             s.add(j)
#             s.add(i // j)
#     count = len(s)
#     if count % 2 == 0:
#         dp[i] = dp[i - 1]
#     else:
#         dp[i] = dp[i - 1] + 1


print(int(8 ** 0.5))