# https://leetcode.com/problems/container-with-most-water/
# Дан массив height длины n
# В нём n вертикальных отрезка, нарисованных таким образом, что, начало отрезка в точке (i, 0), а конец в точке (i, height[i])
# Найдите два отрезка, которые вместе с осью x образуют контейнер, который вмещает в себя наибольшее количество воды,
# среди всех таких контейнеров
# Верните максимальное количество воды, которое может вместить в себя контейнер

# Ограничения:
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# Указание: Вы не можете наклонять контейнер

# Подсказка:
# Используйте метод двух указателей
# На каждом шаге рассчитывайте площадь

# Пример:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

from typing import List

# wrong solutions:

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l, r = 0, 0
#         max_a = 0
#         for r in range(len(height)):
#             a = (r - l) * min(height[l], height[r])
#             while l < r and a < max_a:
#                 l += 1
#                 a = (r - l) * min(height[l], height[r])
#         max_a = max(max_a, a)
#         return max_a

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) - 1
#         max_a = 0
#         while l < r:
#             l_a = (r - l - 1) * min(height[l], height[r - 1])
#             r_a = (r - l - 1) * min(height[l + 1], height[r])
#             a = (r - l) * min(height[l], height[r])
#             mx = max(a, l_a, r_a)
#             if mx == a:
#                 l += 1
#                 r -= 1
#             if mx == r_a:
#                 l += 1
#             if mx == l_a and l_a != r_a:
#                 r -=1
#             max_a = max(max_a, a)

#         return max_a

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_a = 0
        while l < r:
            a = (r - l) * min(height[l], height[r])
            max_a = max(max_a, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_a




if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    height = [2,3,4,5,18,17,6] # 17
    height = [1,8,100,2,100,4,8,3,7] # 200
    result = Solution().maxArea(height)
    print(result)