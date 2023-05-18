# nums = [5, 7, 10, 11, 12, 12, 12]
# nums = [0, 2]
# target = 12
# nums = [5,7,7,8,8,10]
# target = 8

# n = len(nums)

# l, r = 0, n

# while l < r:
#     m = (l + r) // 2
#     if nums[m] >= target:
#         r = m
#     else:
#         l = m + 1

# l1 = l
# print((l, r))

# l, r = -1, n

# while l < r - 1:
#     m = (l + r) // 2
#     if nums[m] <= target:
#         l = m
#     else:
#         r = m - 1

# r1 = l

# print([l1, r1])

# print((l, r))

# if r1 >= l1:
#     print([l1, r1])
# else:
#     print([-1, -1])


# nums = [1,2,3]
# target = 1

nums = []
target = 0

n = len(nums)

l1, r1 = 0, n
l2, r2 = -1, n - 1

while l1 < r1 or l2 < r2:
    if l1 < r1:
        m = (l1 + r1) // 2
        if nums[m] >= target:
            r1 = m
        else:
            l1 = m + 1

    if l2 < r2:
        m = (l2 + r2 + 1) // 2
        if nums[m] <= target:
            l2 = m
        else:
            r2 = m - 1

l, r = l1, l2

if l > r:
    print([-1, -1])
else:
    print([l, r])
