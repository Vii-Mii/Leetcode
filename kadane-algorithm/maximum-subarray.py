class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Brute Force Approach
        # max_sum = nums[0]
        # for i in range(0,len(nums)):
        #     curr_sum = 0 
        #     for j in range(i,len(nums)):
        #         curr_sum += nums[j]
        #         max_sum = max(curr_sum, max_sum)
        # return max_sum

        #Kadanes algorithm
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(curr_sum,0)
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Kadane's Algorithm
# Tags: kadane
