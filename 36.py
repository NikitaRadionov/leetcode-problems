nums = [4, 2, 3, 4]
nums = [2,2,3,4]
nums = [1,2,3,4,5,6]


# Good solution: O(n^2)

nums = sorted(nums)

n = len(nums)

count = 0


for i in range(2, n):

    b = nums[i]

    l = 0
    r = i - 1

    while l < r:

        a = nums[l]
        c = nums[r]

        if a + c > b:
            count += r - l
            r -= 1
        else:
            l += 1

print(count)



# Brute force O(n^3)

# Bad solution O(2^n)

# n = len(nums)
# l, r = 0, n - 1

# def search(l, r):
#     if l < r:
#         l1 = l + 1
#         r1 = r

#         a = nums[l]
#         b = nums[r]

#         while l1 < r1:
#             m = (l1 + r1) // 2
#             c = nums[m]
#             if a + c > b:
#                 r1 = m
#             else:
#                 l1 = m + 1

#         return r - l1
#     else:
#         return 0

# def gen(l, r, s):
#     if l < r:
#         if l + 1 < r:
#             s.add((l + 1, r))
#             gen(l + 1, r, s)
#         if l < r - 1:
#             s.add((l, r - 1))
#             gen(l, r - 1, s)

# s = set()
# s.add((0, n - 1))
# gen(l, r, s)

# s = list(s)

# res = 0
# for i in range(len(s)):
#     l, r = s[i]
#     res += search(l, r)

# print(res)
