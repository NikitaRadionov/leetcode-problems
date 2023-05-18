
with open("txt/20A.txt", "r") as f:
    n = int(f.readline())
    d1 = [-1, -1, -1]
    d2 = [-1, -1, -1]
    sum = 0
    t = None
    last = None
    for i in range(n):
        p = list(map(int, f.readline().split("  ")))
        j = abs(p[0] - p[1]) % 3
        if abs(p[0] - p[1]) < d1[j] or d1[j] == -1:
            t = i
            last = d1[j]
            d1[j] = abs(p[0] - p[1])
            d2[j] = last
        elif abs(p[0] - p[1]) == d1[j] and t != i:
            d2[j] = d1[j]
        elif abs(p[0] - p[1]) < d2[j] and abs(p[0] - p[1]) > d1[j]:
            d2[j] = abs(p[0] - p[1])
        sum += max(p[0], p[1])
print(d2)
print(d1)
k = sum % 3
print(sum)
if k == 0:
    print(sum)
else:
    if k == 1:
        if d2[2] != - 1:
            print(max(sum - d1[k], sum - d1[2] - d2[2]))
        else:
            print(sum - d1[k])
    else:
        if d2[1] != - 1:
            print(max(sum - d1[k], sum - d1[1] - d2[1]))
        else:
            print(sum - d1[k])