class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == int(str(x)[::-1])

# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: Mathematical number property analysis and modular arithmetic.
# Tags: math, optimized
