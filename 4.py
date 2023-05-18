# https://leetcode.com/problems/remove-element/
# Remove Element:
# Задан массив целых чисел nums и целое число val. Удалите все вхождения val в nums "на месте"
# Порядок элементов может быть изменен. Затем верните количество элементов в nums, которые не равны val.

# Учтите, что количество элементов в nums, которые не равны val, равно k, чтобы их приняли, вам нужно выполнить следующие действия:

# Измените массив nums таким образом, чтобы первые k элементов nums содержали элементы, которые не равны val.
# Остальные элементы nums не важны так же, как и размер nums.
# Верните k.

# Примеры:
# Input: nums = [3, 2, 2, 3], val = 3
# Output: 2, nums = [2, 2, '_', '_']

# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: 5, nums = [0, 1, 4, 0, 3, '_', '_', '_']


# "in-place" solution with two pointers l and r


nums = [0, 1, 2, 2, 3, 0, 4, 2]
nums = [1, 1, 1, 1]
val = 1

n = len(nums)

l, k = - 1, 0

for r in range(n):

    if nums[r] != val:
        if l != -1:
            c = nums[l]
            nums[l] = nums[r]
            nums[r] = c
            if nums[l + 1] == "_":
                l += 1
        k += 1

    else:
        nums[r] = "_"
        if l == -1:
            l = r

print(k)
print(nums)