class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0 
        fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
                fast += 1
            else:
                fast += 1
        
        if slow >= len(s):
            return True

        return False

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Fast & slow pointer
# Tags: fast-slow-pointer
