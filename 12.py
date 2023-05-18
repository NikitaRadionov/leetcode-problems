# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/
# Count the Number of Beautiful Subarrays

from operator import xor

# nums = [1,10,4]
# n = len(nums)

# x = 0
# b = {0: [0]}

# for i in range(n):
#     x = xor(x, nums[i])
#     try:
#         b[x].append(i)
#     except KeyError:
#         b[x] = [i + 1]

# count = 0

# res = []

# for k, v in b.items():
#     if len(b[k]) == 2:
#         res.append((v[0], v[1]))

#     if len(b[k]) > 2:
#         m = len(v)
#         for i in range(m - 1):
#             for j in range(i + 1, m):
#                 res.append((v[i], v[j]))

# print(res)


def C(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

nums = [1,10,4]

n = len(nums)

x = 0
b = {0: [0]}

for i in range(n):
    x = xor(x, nums[i])
    try:
        b[x].append(i)
    except KeyError:
        b[x] = [i]

count = 0

for k, v in b.items():
    if len(b[k]) == 2:
        count += 1

    if len(b[k]) > 2:
        m = len(v)
        count += C(m, 2)

print(count)