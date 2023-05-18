# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description/
# Minimum Operations to Make All Array Elements Equal

# nums = [3, 1, 6, 8]
# queries = [1, 5]

# O((m + n)log(n))

nums = [2,9,6,3]
queries = [10]

nums = sorted(nums)
n = len(nums)

b = [0]

for i in range(n):
    b.append(b[i] + nums[i])

answer = []

for q in queries:

    l = -1
    r = n

    while l < r - 1:
        i = (l + r) // 2
        if nums[i] > q:
            r = i
        else:
            l = i

    sum = abs(q*r - b[r]) + abs(q * n - q *r - b[n] + b[r])
    answer.append(sum)

print(answer)


# brute force O(nm)
# class Solution:
#     def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
#         answer = []

#         for q in queries:

#             sum = 0
#             for e in nums:
#                 sum += abs(e - q)
#             answer.append(sum)

#         return answer