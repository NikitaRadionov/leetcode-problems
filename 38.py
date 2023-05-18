with open('txt/38B.txt', 'r') as f:
    n = int(f.readline())
    nums = [int(_) for _ in f]

nums = sorted(nums)

s1 = [0, 0, 0]
s2 = [0, 0, 0]

i, j, k, d = n - 1, 0, 0, 0

while -1 < i and (j < 3 or k < 3 or d < 1):

    if nums[i] % 3 == 0 and j < 3:
        s1[j] = nums[i]
        j += 1

    if nums[i] % 3 == 1 and k < 3:
        s2[k] = nums[i]
        k += 1

    if nums[i] % 3 == 2 and d < 1:
        m2 = nums[i]
        d += 1

    i -= 1

mx = max(s1[0] + s1[1] + s1[2], s2[0] + s2[1] + s2[2], s1[0] + m2 + s2[0])

print(mx)
