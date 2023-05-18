# https://leetcode.com/problems/rotate-array/
# Rotate Array:
# Задан целочисленный массив nums. Сделайте его перестановку k раз вправо "in-place"

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

#

from typing import List

# O(nk) - worst
# O(n) - average

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        n = len(nums)
        d = gcd(n, k)
        x = 1
        while (k * x) % n != 0:
            x += 1
        for i in range(d):
            for j in range(x - 1):
                c = nums[(i - k * j) % n]
                nums[(i - k * j) % n] = nums[(i - k * (j + 1)) % n]
                nums[(i - k * (j + 1)) % n] = c
        return nums


# Always O(nk) time
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(k):
            for j in range(n - 1, 0, -1):
                c = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = c
        return nums



numss = [[1,2,3,4,5,6,7], [-1,-100,3,99], [1,2,3,4,5,6,7], [1], [1,2,3,4,5,6], [1, 2, 3, 4, 5 ,6]]
ks =[3, 2, 0, 0, 3, 2]
answers = [[5, 6, 7, 1, 2, 3, 4], [3,99,-1,-100], [1,2,3,4,5,6,7], [1], [4, 5, 6, 1, 2, 3], [5, 6, 1, 2, 3, 4]]

for i in range(len(numss)):
    res = Solution().rotate(numss[i], ks[i])
    if res == answers[i]:
        print('OK')
    else:
        print(f"WRONG ANSWER: expected: {answers[i]} output: {res}")