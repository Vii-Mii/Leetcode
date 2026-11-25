class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr_max = curr_min = 1

        for i in nums:
            temp = curr_max * i
            curr_max = max(curr_min * i, temp, i)
            curr_min = min(curr_min * i, temp, i)

            res = max(res, curr_max)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimal solution implementing algorithms technique.
# Tags: array, optimized
