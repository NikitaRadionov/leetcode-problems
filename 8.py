# Вам даны два массива целых чисел nums1 и nums2, отсортированные в порядке неубывания, и два целых числа m и n,
# представляющих количество элементов в nums1 и nums2 соответственно.

# Объедините nums1 и nums2 в единый массив, отсортированный в порядке неубывания.

# Окончательный отсортированный массив не должен быть возвращен функцией, а вместо этого сохранен внутри массива nums 1.
# Чтобы учесть это, nums1 имеет длину m + n, где первые m элементов обозначают элементы,
# которые должны быть объединены, а последние n элементов установлены в 0 и должны игнорироваться. nums2 имеет длину n.

from typing import List

# m, n = 1, 5

# nums1 = [4, 0, 0, 0, 0, 0]
# nums2 = [1, 2, 3, 5, 6]

# m, n = 4, 3
# nums1 = [-3, 0, 6, 9, 0, 0, 0]
# nums2 = [-4, 2, 8]

# m, n = 6, 3
# nums1 = [-1,0,0,3,3,3,0,0,0]
# nums2 = [1,2,2]

# m, n = 3, 6
# nums1 = [0,0,3,0,0,0,0,0,0]
# nums2 = [-1,1,1,1,2,3]

# m, n = 2, 5
# nums1 = [-1,3,0,0,0,0,0]
# nums2 = [0,0,1,2,3]

# m, n = 4, 2
# nums1 = [-1,-1,0,0,0,0]
# nums2 = [-1,0]

m, n = 12, 9
nums1 = [-1, -1, -1, -1, 0, 0, 0, 2, 2, 2, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nums2 = [-1, -1, -1, 1, 1, 1, 3, 3, 3]

print(len(nums1), len(nums2))

l, r = m - 1, n - 1
k = m + n - 1

while r >= 0:
    print(nums1)
    print(nums2)
    print(f'L = {l}, R = {r}')
    print()
    if l >=0 and nums1[l] > nums2[r]:
        nums1[k] = nums1[l]
        l -= 1
    else:
        nums1[k] = nums2[r]
        r -= 1
    k -= 1

print(nums1)




# fuck this bullshit
# l, r = 0, 0
# while l < n + m and r < n:
#     print(nums1)
#     print(nums2)
#     print(f'L = {l}, R = {r}')
#     print()

#     if nums2[r] > nums1[l]:

#         if m == 0 or 0 < l and (nums1[l - 1] > nums1[l] or l >= m):
#             c = nums2[r]
#             nums2[r] = nums1[l]
#             nums1[l] = c
#             r += 1

#         l += 1
#         continue

#     if nums2[r] < nums1[l]:

#         c = nums2[r]
#         nums2[r] = nums1[l]
#         nums1[l] = c
#         l += 1
#         i = r
#         while i < n - 1 and nums2[i] > nums2[i + 1]:
#             c = nums2[i]
#             nums2[i] = nums2[i + 1]
#             nums2[i + 1] = c
#             i += 1
#         continue

#     if nums2[r] == nums1[l]:
#         if m < l + 1 < m + n and nums1[l + 1] == nums1[l]:
#             r += 1
#         l += 1
#         continue

# print(nums1)
# print(nums2)


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         l, r = 0, 0
#         while l < n + m and r < n:

#             if nums2[r] >= nums1[l]:

#                 if m == 0 or 0 < l and nums1[l - 1] > nums1[l]:
#                     c = nums2[r]
#                     nums2[r] = nums1[l]
#                     nums1[l] = c
#                     r += 1

#                 l += 1
#                 continue

#             if nums2[r] < nums1[l]:

#                 c = nums2[r]
#                 nums2[r] = nums1[l]
#                 nums1[l] = c
#                 l += 1
#                 i = r
#                 while i < n - 1 and nums2[i] > nums2[i + 1]:
#                     c = nums2[i]
#                     nums2[i] = nums2[i + 1]
#                     nums2[i + 1] = c
#                     i += 1
#         return nums1


# mns = [
#     (3, 3),
#     (0, 1),
#     (1, 0),
#     (4, 3),
#     (4, 3),
# ]

# nums1s = [
#     [1, 2, 3, 0, 0, 0],
#     [0],
#     [1],
#     [-3, 0, 6, 9, 0, 0, 0],
#     [-3, -2, 6, 9, 0, 0, 0],
# ]

# nums2s = [
#     [2, 5, 6],
#     [1],
#     [],
#     [-4, 2, 8],
#     [-4, 2, 8]
# ]

# answers = [
#     [1, 2, 2, 3, 5, 6],
#     [1],
#     [1],
#     [-4, -3, 0, 2, 6, 8, 9],
#     [-4, -3, -2, 2, 6, 8, 9],
# ]

# for i in range(len(mns)):
#     m, n = mns[i]
#     res = Solution().merge(nums1s[i], m, nums2s[i], n)
#     if res == answers[i]:
#         print('OK')
#     else:
#         print(f"WRONG ANSWER: expected: {answers[i]}, output: {res}")