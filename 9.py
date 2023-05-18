# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0]

# nums = [0,0,0,0]


# Time Limit Exceeded

nums = [-1,0,1,2,-1,-4]

nums = sorted(nums)

n = len(nums)

res = []

for z in range(n - 2):

    l = z + 1
    r = n - 1

    while l < r:
        a = nums[l]
        b = nums[r]
        c = nums[z]

        if a + b + c > 0:
            r -= 1

        if a + b + c < 0:
            l += 1

        if a + b + c == 0:
            if not ((a, c, b) in res or (a, b, c) in res or (b, a, c) in res or (b, c, a) in res or (c, a, b) in res or (c, b, a) in res):
                res.append((a, c, b))
            l += 1

print(res)



#Fuck this shit

# class Tulip:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __hash__(self):
#         sum = self.a ** 3 + self.b ** 3 + self.c ** 3
#         return hash(sum)

#     def __eq__(self, other):
#         return hash(self) == hash(other)

#     def __str__(self):
#         return str((self.a, self.b, self.c))

#     __repr__ = __str__

# def lst(obj):
#     return [obj.a, obj.b, obj.c]

# nums = [1,2,-2,-1]

# nums = [-1,0,1,2,-1,-4]

# nums = sorted(nums)

# n = len(nums)

# res = set()

# for z in range(n - 2):

#     l = z + 1
#     r = n - 1

#     while l < r:
#         a = nums[l]
#         b = nums[r]
#         c = nums[z]

#         if a + b + c > 0:
#             r -= 1

#         if a + b + c < 0:
#             l += 1

#         if a + b + c == 0:
#             res.add(Tulip(a, b, c))
#             l += 1

# print(list(map(lst, res)))






#Solution from random user
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         res = set()

#         #1. Split nums into three lists: negative numbers, positive numbers, and zeros
#         n, p, z = [], [], []
#         for num in nums:
#             if num > 0:
#                 p.append(num)
#             elif num < 0:
#                 n.append(num)
#             else:
#                 z.append(num)

#         #2. Create a separate set for negatives and positives for O(1) look-up times
#         N, P = set(n), set(p)

#         #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
#         #   i.e. (-3, 0, 3) = 0
#         if z:
#             for num in P:
#                 if -1*num in N:
#                     res.add((-1*num, 0, num))

#         #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
#         if len(z) >= 3:
#             res.add((0,0,0))

#         #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
#         #   exists in the positive number set
#         for i in range(len(n)):
#             for j in range(i+1,len(n)):
#                 target = -1*(n[i]+n[j])
#                 if target in P:
#                     res.add(tuple(sorted([n[i],n[j],target])))

#         #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
#         #   exists in the negative number set
#         for i in range(len(p)):
#             for j in range(i+1,len(p)):
#                 target = -1*(p[i]+p[j])
#                 if target in N:
#                     res.add(tuple(sorted([p[i],p[j],target])))

#         return res


# Just for fun
# nums = [-1,0,1,2,-1,-4]

# nums = sorted(nums)

# n = len(nums)

# l, r, z = 0, n - 1, 1

# res = []

# while z < r:
#     a = nums[l]
#     b = nums[r]
#     c = nums[z]

#     if a + b + c > 0:
#         r -= 1

#     if a + b + c < 0:
#         l += 1
#         if z == l:
#             z += 1

#     if a + b + c == 0:
#         if not ((a, c, b) in res or (a, b, c) in res or (b, a, c) in res or (b, c, a) in res or (c, a, b) in res or (c, b, a) in res):
#             res.append((a, c, b))
#         z += 1