class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_string = {}
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    sub_string[len(s[i:j])]= s[i:j]
        return sub_string[max(sub_string.keys())]

# Time Complexity: O(n²)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
