# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Find the Index of the First Occurrence in a String
# Даны две строки: needle и haystack. Верните индекс первого вхождения needle в haystack или -1, если needle нет в haystack

# Органичения:
# 1 <= len(haystack), len(needle) <= 10**4
# haystack и needle содержат только английские буквы в нижнем регистре

# Примеры:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

# fucking two pointers solution:
# Worst: O(nm)
# Average: O(n)
# Memory: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        l, min_i, i = 0, n + 1, -1
        total_match = 0

        if m > n:
            return -1

        for r in range(n):

            if l < m and haystack[r] == needle[l]:
                l += 1
                total_match += 1
                if i == -1:
                    i = r
                if total_match == m:
                    min_i = min(min_i, i)
            else:
                i = -1
                total_match = 0
                if r > 0 and l > 0:
                    j = 0
                    while j < m and haystack[r] != needle[j]:
                        j += 1
                    if j < m and j <= r:
                        total_match = 1
                        k = 0
                        while k < j and haystack[r - j + k] == needle[k]:
                            total_match += 1
                            k += 1
                        if k == j:
                            i = r - j
                            l = j + 1
                        else:
                            total_match = 0
                            i = -1
                            l = 0
                    else:
                        i = -1
                        l = 0

        if min_i == n + 1:
            min_i = -1

        return min_i


haystacks = ["sadbutsad", "leetcode", "butsadsad", 's', 'mississippi', 'mississippi', 'mississippi', "babbbbbabb"]
needles = ["sad", "leeto", "sad", 's', 'issip', 'issi', 'sippi', "bbab"]
answers = [0, -1, 3, 0, 4, 1, 6, 5]

for i in range(len(haystacks)):
    if i == 7:
        print()
    res = Solution().strStr(haystacks[i], needles[i])
    if res == answers[i]:
        print('OK')
    else:
        print(f"WRONG ANSWER: expected: {answers[i]} output: {res}")


# Time: O(n + m)
# Memory: O(n + m)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         def z_func(s:str) -> list:
#             n = len(s)
#             z = [0] * n
#             l = 0
#             r = 0
#             for i in range(1, n):
#                 if i <= r:
#                     z[i] = min(r - i + 1, z[i - l])
#                 while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#                     z[i] += 1
#                 if (i + z[i] - 1 > r):
#                     l = i
#                     r = i + z[i] - 1
#             return z

#         min_i = len(haystack) + 1
#         s = needle + "#" + haystack
#         z = z_func(s)
#         p = len(needle)
#         count = 0
#         for i in range(len(haystack)):
#             if z[i + p + 1] == p:
#                 min_i = i
#                 break

#         if min_i == len(haystack) + 1:
#             min_i = -1

#         return min_i



# haystacks = ["sadbutsad", "leetcode", "butsadsad", 's', 'mississippi', 'mississippi', 'mississippi', "babbbbbabb"]
# needles = ["sad", "leeto", "sad", 's', 'issip', 'issi', 'sippi', "bbab"]
# answers = [0, -1, 3, 0, 4, 1, 6, 5]

# for i in range(len(haystacks)):
#     if i == 0:
#         print()
#     res = Solution().strStr(haystacks[i], needles[i])
#     if res == answers[i]:
#         print('OK')
#     else:
#         print(f"WRONG ANSWER: expected: {answers[i]} output: {res}")
