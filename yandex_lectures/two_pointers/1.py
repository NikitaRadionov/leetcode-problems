# Дана отсортированная последовательность чисел длиной N и число K
# Необходимо найти количество пар чисел A, B, таких что B - A > K.

# Примеры:
# Input: lst = [1, 3, 7, 8], K = 4
# Output: 3

# Решение за O(n^2)
# Перебираем все пары чисел и для каждой проверим условие B - A > K

def solution1():
    lst = [1, 3, 7, 8]
    K = 4
    N = len(lst)

    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            a = lst[i]
            b = lst[j]
            if b - a > K:
                count += 1

    print(count)


def solution2():

    lst = [1, 3, 7, 8]
    K = 4
    N = len(lst)

    count = 0
    for l in range(N - 1):
        r = l + 1
        while r < N and lst[r] - lst[l] <= K:
            r += 1
        if r < N:
            count += N - r

    print(count)


# Решение за O(n)
lst = [1, 3, 7, 8]
K = 4
N = len(lst)

count = 0
r = 1
for l in range(N - 1):
    while r < N and lst[r] - lst[l] <= K:
        r += 1
    count += N - r

print(count)

