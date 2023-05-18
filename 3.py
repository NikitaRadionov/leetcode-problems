# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Remove Duplicates from Sorted Array
# Задан массив nums, состоящий из целых чисел, который отсортирован в порядке неубывания.
# Удалите повторы "на месте" такие, что каждый уникальный элемент появляется только один раз.
# Относительный порядок элементов должен быть сохранен.
# Верните количество уникальных элементов в массиве nums

# Измените массив nums таким образом, чтобы первые k элементов nums содержали уникальные элементы в том порядке,
# в котором они присутствовали в nums изначально. Остальные элементы nums не важны так же, как и размер nums.


# Ограничения:
# 1 <= len(nums) <= 3*10**4
# -100 <= nums[i] <= 100
# nums отсортирован в порядке невозрастания


# Примеры:
# Input: nums = [1, 1, 2]
# Output: 2, nums = [1, 2, _]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# no "in-place" solution:

# nums = [1, 1, 2]
# nums = [0,0,1,1,1,2,2,3,3,4]

# n = len(nums)

# last = 101
# result = []
# k = 0

# for i in range(n):

#     if nums[i] != last:
#         last = nums[i]
#         result.append(last)
#         k += 1

#         j = 0

# while j < n:
#     if j < k:
#         nums[j] = result[j]
#     else:
#         nums[j] = '_'
#     j += 1


# print(nums)
# print(k)


# "in-place" solution with two pointers


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1,1,2]
nums = [1, 2, 3]
nums = [1, 2, 2]

n = len(nums)

last, l, k = nums[0], -1, 1

for r in range(1, n):

    if nums[r] != last:
        if l != -1:
            last = nums[r]
            nums[r] = nums[l]
            nums[l] = last
            if nums[l + 1] == "_":
                l += 1
        else:
            last = nums[r]
        k += 1
    else:
        nums[r] = "_"
        if l == -1:
            l = r

print(nums)
print(k)
