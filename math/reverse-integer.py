class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        val = 1 if x >0 else -1

        x = val * x
        while x:
            digit = x % 10
            res = res * 10 + digit

            if res > 2**31-1 or res < -1*(2**31):
                return 0
            x //= 10

        return val * res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Mathematical number property analysis and modular arithmetic.
# Tags: math, optimized
