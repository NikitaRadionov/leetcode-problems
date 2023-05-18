with open("txt/21B.txt", "r") as f:
    n = int(f.readline())
    k = 43
    mins = [(None, None) for _ in range(k)]
    s, mx, lght = 0, 0, -1
    for i in range(n):
        a = int(f.readline())
        s += a
        m, l = mins[s % k]
        if (not (m is None or l is None)) and (s - m > mx or s - m == mx and lght > i - l + 1):
            mx = s - m
            lght = i - l
        if m is None and l is None:
            mins[s % k] = (s, i)
    print(lght)







# with open("txt/21B.txt", "r") as f:
#     n = int(f.readline())
#     k = 43
#     d = { i: [] for i in range(k) }
#     b = [0 for _ in range(n + 1)]
#     m = 0
#     lght = 0
#     for i in range(n):
#         a = int(f.readline())
#         b[i + 1] = b[i] + a
#         for l in d[b[i + 1] % k]:
#             r = i + 1
#             if m < b[r] - b[l] or m == b[r] - b[l] and lght > r - l:
#                 m = b[r] - b[l]
#                 lght = r - l
#         d[b[i + 1] % k].append(i)
#     print(lght)
