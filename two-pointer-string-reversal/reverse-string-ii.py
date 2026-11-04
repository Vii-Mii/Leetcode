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

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0,len(s),2*k):
            left = i
            right = min(i+k-1,len(s)-1)
            while left <= right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return "".join(s)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two pointer String reversal
#     looping the array with 2k
#     placing pointer left as i and right as min of i+k-1 (swapping range) or len(s)-1 for the last value coverage
#     reversing the left to right
# Tags: two-pointer, optimized
