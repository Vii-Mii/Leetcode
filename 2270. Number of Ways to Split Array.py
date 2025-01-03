class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        final = 0
        track = 0
        total_sum = sum(nums)
        for i in range(len(nums)-1):
            track += nums[i]
            check = total_sum - track
            if  track >= check:
                final += 1
        return final


# Time Complexity : O(n)
# Space Complexity: O(1)
