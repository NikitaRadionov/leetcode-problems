
# Слить две отсортированные последовательности чисел
# в одну.


first = [1, 2, 5, 7]
second = [3, 4, 4]

result = []

n, m = len(first), len(second)
i, j = 0, 0

while i < n and j < m:
    if first[i] <= second[j]:
        result.append(first[i])
        i += 1
    else:
        result.append(second[j])
        j += 1

while i < n:
    result.append(first[i])
    i += 1

while j < m:
    result.append(second[j])
    j += 1

print(result)


