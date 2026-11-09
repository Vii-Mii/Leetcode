class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        return max_count

# Time Complexity: O(n)
# Space Complexity: O(n)
# Tags: brute-force
