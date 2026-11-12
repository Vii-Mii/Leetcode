class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in window:
                length = max(length, r-l)
                index = window.index(s[r])
                window = window[index+1:]
                l += index + 1
            window.append(s[r])
            length = max(length, len(window))
        return len(window) if length == 0 else length

# Time Complexity: O(n)
# Space Complexity: O(n)
# Tags: sliding-window
