class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
        
        for j in t:
            if j not in count_s or count_s[j] == 0:
                return False
            if count_s[j] > 0:
                count_s[j] -= 1
        
        if sum(count_s.values()):
            return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
        
        for j in t:
            if j not in count_s or count_s[j] == 0:
                return False
            if count_s[j] > 0:
                count_s[j] -= 1
        
        if sum(count_s.values()):
            return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hash Map / Set lookup storing frequencies or previous values for O(1) average-time queries.
# Tags: hashing, optimized
