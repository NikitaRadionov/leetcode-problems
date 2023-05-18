
with open("19B.txt", "r") as file:
    n = int(file.readline())
    s = 0
    d = [0 for _ in range(999)]
    count = 0
    for i in range(n):
        a = int(file.readline())
        s = (s + a) % 999
        if s == 0:
            count += 1
        count += d[s]
        d[s] += 1

print(count)

# with open("19B.txt", "r") as file:
#     n = int(file.readline())
#     s = 0
#     d = {i: [] for i in range(999)}
#     for i in range(n):
#         a = int(file.readline())
#         s = (s + a) % 999
#         d[s].append(i)

# res = 0
# for key, value in d.items():
#     k = len(value)
#     if k > 1:
#         res += (k * (k - 1)) // 2
#         if key == 0:
#             res += k

# print(res)



# with open("19B.txt", "r") as file:
#     n = int(file.readline())
#     s = 0
#     d = [0 for _ in range(999)]
#     count = 0
#     for i in range(n):
#         a = int(file.readline())
#         s = (s + a) % 999
#         if s == 0:
#             count += 1
#         # count += d[s]
#         d[s] += 1

# res = 0
# for i in range(999):
#     if d[i] > 1:
#         v = d[i]
#         res += v * (v - 1) // 2
# print(res + count)