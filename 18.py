import sys



def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))

    if n > 2:

        dp = [-1, a[1] - a[0], a[2] - a[0]]

        for i in range(3, n):
            dp.append(min(dp[i - 1], dp[i - 2]) + a[i] - a[i - 1])

        print(dp[n - 1])

    else:
        print(a[1] - a[0])

if __name__ == '__main__':
	main()



# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#     a = sorted(a)
#     d = [a[0]] + [a[i] - a[i - 1] for i in range(1, n)]
#     s = {1, n - 1}

#     for i in range(2, n - 2):
#         if i == 1 or i == n - 1:
#             s.add(i)
#         else:
#             m = min(d[i], d[i + 1])
#             if m == d[i]:
#                 s.add(i)
#             if m == d[i + 1]:
#                 s.add(i + 1)
#     sum = 0
#     for i in s:
#         sum += d[i]
#     print(sum)

# if __name__ == '__main__':
# 	main()


# def main():
#     n = int(input())
#     a = list(map(lambda x: [int(x), False], input().split()))
#     a = sorted(a, key=lambda x: x[0])

#     sum = 0
#     for i in range(n):
#         if not a[i][1]:
#             x = a[i][0]
#             if i == n - 1:
#                 sum += x - a[i - 1][0]
#             elif i == 0:
#                 sum += a[i + 1][0] - x
#                 a[i + 1][1] = True
#             elif a[i + 1][0] - x == 1:
#                 sum += 1
#                 a[i + 1][1] = True
#             else:
#                 y = a[i + 1][0]
#                 z = a[i - 1][0]
#                 if y - x <= x - z:
#                     sum += y - x
#                     a[i + 1][1] = True
#                 else:
#                     sum += x - z
#             a[i][1] = True
#     print(sum)

# if __name__ == '__main__':
# 	main()