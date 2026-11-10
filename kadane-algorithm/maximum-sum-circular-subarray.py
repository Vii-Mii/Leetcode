class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        currMax, currMin = 0,0
        globalMax, globalMin = nums[0],nums[0]
        total = 0

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        if globalMax > 0:
            return max(globalMax, total - globalMin)
        return globalMax

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Kadane's algorithm
# Tags: kadane
