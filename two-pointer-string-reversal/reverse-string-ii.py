class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        val = 0 
        s = list(s)

        for i in range(0,len(s),k):
            if val % 2 == 0:
                s[i:i+k] = s[i:i+k][::-1]
                val += 1
            else:
                val += 1
        return "".join(s)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Brute Force approach with string slicing with the val increment
# Tags: brute-force
