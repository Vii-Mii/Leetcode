class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total, l = 0, 0
        length = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = min(length, r-l+1)
                total -= nums[l]
                l += 1
        
        return 0 if length == float('inf') else length

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: sliding window
# Tags: sliding-window
