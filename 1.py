# x - integer
# return true if x is a palindrome and false otherwise.
# -2^31 <= x <= 2^31 - 1
# solve it without converting the integer to a string
# Wanted complexity: O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        a = x
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        
        print(f"result: {result}")

        return True if result == a else False


if __name__ == "__main__":
    x = int(input())
    result = Solution().isPalindrome(x)
    print(result)