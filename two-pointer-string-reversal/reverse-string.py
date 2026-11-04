class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 
        right = len(s)-1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two pointer (Reversal pattern)
#     Swapping variables
# Tags: two-pointer, brute-force
