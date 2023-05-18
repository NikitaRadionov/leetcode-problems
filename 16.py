# https://leetcode.com/problems/find-all-good-indices/
# Find All Good Indices

# nums = [2,1,1,1,3,4,1]
# nums = [2,1,1,2]
# nums = [478184,863008,716977,921182,182844,350527,541165,881224]
# k = 1

# Good solution O(n) - time and O(n) - memory

nums = [2, 1, 1, 1, 3, 4, 1]

k = 2

n = len(nums)

decrease= [1 for _ in range(n + 1)]
increase = [1 for _ in range(n + 1)]

for i in range(n):
    if nums[i - 1] >= nums[i]:
        decrease[i] = decrease[i - 1] + 1

for i in range(n - 2, -1, -1):
    if nums[i] <= nums[i + 1]:
        increase[i] = increase[i + 1] + 1

res = []
for i in range(k, n - k):
    if decrease[i - 1] >= k and increase[i + 1] >= k:
        res.append(i)

print(res)

# Bad solution for O(nk) time. Time Limit Exceeded

# nums = [253747,459932,263592,354832,60715,408350,959296]
# k = 2

# n = len(nums)

# if k > 1:

#     a = [nums[0]] + [nums[i] - nums[i - 1] for i in range(1, n)]
#     print(a)

#     res = []

#     for i in range(k, n - k):
#         cl, cr = 0, 0
#         for j in range(i - k + 1, i):
#             if a[j] <= 0:
#                 cl += 1
#         for j in range(i + 2, i + k + 1):
#             if a[j] >= 0:
#                 cr += 1
#         if cl + cr == 2*k - 2:
#             res.append(i)

#     print(res)
# else:
#     print(list(range(k, n - k)))