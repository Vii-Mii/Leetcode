class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        zeros, ones = 0,0

        for i in s:
            if i == "1":
                ones += 1
            else:
                swap += ones
                zeros += 1
        return swap

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimised Approach
#     count zeros & ones
#     add ones before every zeros when swap
# Tags: two-pointer
