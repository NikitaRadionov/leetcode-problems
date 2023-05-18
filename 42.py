nums = [1, 2, 3, 4, 5]
x = 3
k = 4


def shortest(a, b, x):
    return abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b)


n = len(nums)

l = 0
r = n - 1


while l < r:
    m = (l + r + 1) // 2
    if nums[m] <= x:
        l = m
    else:
        r = m - 1

i = l


left = i - 1 if i - 1 > -1 else None
right = i + 1 if i + 1 < n else None
res = []

if not(right is None):

    if shortest(nums[right], nums[l], x):
        left = i
        i = right
        right = i + 1 if i + 1 < n else None

j = 0

while j < k:
    res.append(nums[i])
    j += 1

    if (not (left is None)) and ((right is None) or shortest(nums[left], nums[right], x)):
        i = left
        left = i - 1 if i - 1 > -1 else None
    elif not (right is None):
        i = right
        right = i + 1 if i + 1 < n else None

res.sort()

print(res)
