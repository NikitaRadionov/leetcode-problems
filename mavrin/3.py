# https://codeforces.com/group/pgkaqF4igo/contest/256854/problem/C
# Три части массива

n = int(input())
d = list(map(int, input().split()))

s1 = 0
s2 = 0
r = n
max_sum = 0

for l in range(n):
    s1 += d[l]
    while s1 > s2:
        r -= 1
        s2 += d[r]

    if s1 == s2 and r > l:
        max_sum = max(max_sum, s1)

print(max_sum)