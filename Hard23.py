def intt(s: str) -> int:
    if s == "":
        return 0
    else:
        return int(s)

# s = "1000"
# k = 10000

s = "1000"
k = 10

# s = "1"
# k = 1

# s = "1317"
# k = 2000

# s = "1234"
# k = 1000

# s = "5"
# k = 3

# s = "5"
# k = 9

# s = "1234"
# k = 123

# s = "1234"
# k = 12

# s = "1234"
# k = 1

# s = "1234"
# k = 9


# s = "1234"
# k = 12

n = len(s)
m = len(str(k))

dp = [0 for i in range(n)]
b = ["" for i in range(n + 1)]

dp[0] = 1

if n < m:
    for i in range(1, n):
        if s[i] == "0":
            dp[i] = dp[i - 1]
        elif s[i - 1] == "0":
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 2 * dp[i - 1]

    print(dp[n - 1])


if n == m and 1 <= k <= 9:
    if int(s) <= k:
        print(1)
    else:
        print(0)


if n == m and k > 9:
    for i in range(1, n - 1):
        if s[i] == "0":
            dp[i] = dp[i - 1]
        elif s[i - 1] == "0":
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 2 * dp[i - 1]

    if int(s) <= k:
        i = n - 1
        if s[i] == "0":
            dp[i] = dp[i - 1]
        elif s[i - 1] == "0":
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 2 * dp[i - 1]
    else:
        if s[n - 2] == "0" or s[n - 1] == "0":
            dp[n - 1] = dp[n - 2]
        else:
            dp[n - 1] = 2 * dp[n - 2] - 1

    print(dp[n - 1])



if n > m:
    t = 1
    for i in range(n):
        if i < m:
            t *= 10
        b[i + 1] = b[i] + s[i]

    for i in range(1, m - 1):
        if s[i] == "0":
            dp[i] = dp[i - 1]
        elif s[i - 1] == "0":
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 2 * dp[i - 1]

    p = m - 1 if m > 1 else 1

    for i in range(p, n):
        if intt(b[i + 1]) - intt(b[i - m + 1]) * t <= k:
            if s[i] == "0":
                dp[i] = dp[i - 1]
            elif s[i - 1] == "0":
                dp[i] = dp[i - 1] + 1
            else:
                if dp[i - 1] > 2 * dp[i - 1] - i + m - 1:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = 2 * dp[i - 1] - i + m - 1
        else:
            if s[i - 1] == "0" or s[i] == "0":
                dp[i] = dp[i - 1]
            else:
                if dp[i - 1] > 2 * dp[i - 1] - i + m - 2:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = 2 * dp[i - 1] - i + m - 2

    print(dp[n - 1])





# def intt(s: str) -> int:
#     if s == "":
#         return 0
#     else:
#         return int(s)

# # s = "1000"
# # k = 10000

# s = "1000"
# k = 10

# # s = "1317"
# # k = 2000

# n = len(s)
# m = len(str(k))

# dp = [0 for i in range(n)]
# b = ["" for i in range(n + 1)]

# dp[0] = 1

# if n < m:
#     for i in range(1, n):
#         if s[i] == "0":
#             dp[i] = dp[i - 1]
#         elif s[i - 1] == "0":
#             dp[i] = dp[i - 1] + 1
#         else:
#             dp[i] = 2 * dp[i - 1]

#     print(dp[n - 1])


# if n == m and 1 <= k <= 9:
#     if int(s) <= k:
#         print(1)
#     else:
#         print(0)


# if n == m and k > 9:
#     for i in range(1, n - 1):
#         if s[i] == "0":
#             dp[i] = dp[i - 1]
#         elif s[i - 1] == "0":
#             dp[i] = dp[i - 1] + 1
#         else:
#             dp[i] = 2 * dp[i - 1]

#     if int(s) <= k:
#         i = n - 1
#         if s[i] == "0":
#             dp[i] = dp[i - 1]
#         elif s[i - 1] == "0":
#             dp[i] = dp[i - 1] + 1
#         else:
#             dp[i] = 2 * dp[i - 1]
#     else:
#         if s[n - 2] == "0" or s[n - 1] == "0":
#             dp[n - 1] = dp[n - 2]
#         else:
#             dp[n - 1] = 2 * dp[n - 2] - 1

#     print(dp[n - 1])



# if n > m:
#     t = 1
#     for i in range(n):
#         if i < m:
#             t *= 10
#         b[i + 1] = b[i] + s[i]

#     for i in range(1, m - 1):
#         if s[i] == "0":
#             dp[i] = dp[i - 1]
#         elif s[i - 1] == "0":
#             dp[i] = dp[i - 1] + 1
#         else:
#             dp[i] = 2 * dp[i - 1]

#     for i in range(m - 1, n):
#         if intt(b[i + 1]) - intt(b[i - m + 1]) * t <= k:
#             if s[i] == "0":
#                 dp[i] = dp[i - 1]
#             elif s[i - 1] == "0":
#                 dp[i] = dp[i - 1] + 1
#             else:
#                 dp[i] = 2 * dp[i - 1] - i + m - 1
#         else:
#             if s[i - 1] == "0" or s[i] == "0":
#                 dp[i] = dp[i - 1]
#             else:
#                 dp[i] = 2 * dp[i - 1] - i + m - 2

#     print(dp[n - 1])
