# https://codeforces.com/group/pgkaqF4igo/contest/256854/problem/A
# Книги:
# t - кол-во минут
# n - кол-во книг
# a = [-1, a1, a2, a3, a4, ... , an]
# a[i] - кол-во минут на чтение этой книги, i in [1:n]
# Человек читает книгу начиная с i-ой и до того момента как он либо прочтет n-ую книгу, либо закончится время t
# Посчитать максимальное кол-во книг, которое можно прочесть за промежуток времени t
#


def solution(n, t, a):
    l = 0
    s = 0
    res = 0
    for r in range(n):
        s += a[r]
        while l < r and (s > t):
            s -= a[l]
            l += 1
        res = max(res, r - l + 1)
    return res



if __name__ == "__main__":
    n = 4
    t = 5
    a = [3, 1, 2, 1]
    result = solution(n, t, a)
    print(result)