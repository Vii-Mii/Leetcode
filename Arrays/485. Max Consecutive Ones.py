from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        val = 0
        for i in nums:
            if i == 1:
                val += 1
            else:
                val = 0
            max_ones = max(max_ones,val)

        return max_ones

# Time complexity : O(n)
# Space complexity : O(1)