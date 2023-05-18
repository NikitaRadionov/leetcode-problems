nums = [1,3,5,6]
target = 5

n = len(nums)
l = 0
r = n

while l < r:
    m = (l + r) // 2
    if nums[m] >= target:
        r = m
    else:
        l = m + 1

print(l)