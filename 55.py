
a = [1, 2, 3, -10, 2, 3, -3]
b = [0 for _ in range(len(a) + 1)]
l = 0
mn, mx = None, None

for i in range(len(a)):
    b[i + 1] = b[i] + a[i]
    if mx is None or mx < b[i + 1] - b[l]:
        mx = b[i + 1] - b[l]
        r = i + 1

    if mn is None or mn > b[i + 1]:
        mn = b[i + 1]
        l = i + 1


print(f"[{l}, {r})")