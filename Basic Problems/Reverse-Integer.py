class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        res = 0
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        res *= sign
        if res > 2**31-1 or res < -2**31:
            return 0
        return res