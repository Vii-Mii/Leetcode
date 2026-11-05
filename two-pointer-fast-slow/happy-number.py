class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()

        while n != 1:
            if n in values:
                return False
            values.add(n)
            val = sum([int(i)**2 for i in str(n)])
            n = val
        
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Brute force approach with set
# Tags: hashing
