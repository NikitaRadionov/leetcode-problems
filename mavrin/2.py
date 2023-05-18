# https://codeforces.com/group/pgkaqF4igo/contest/256854/problem/B
# Сбалансированная команда

n = int(input())
a = list(map(int, input().split()))

l = 0
max_count = 0
count = 0

a = sorted(a)

for r in range(n):
    count += 1
    while a[r] - a[l] > 5:
        l += 1
        count -= 1
    max_count = max(max_count, count)

print(max_count)