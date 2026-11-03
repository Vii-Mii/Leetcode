class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        values = {}
        for i in range(len(nums)):
            if target - nums[i] in values:
                return [values[target - nums[i]],i]
            else:
                values[nums[i]] =  i
        return [0,0]

#new version

/*
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Approach: Hash map approach
 * Tags: two-pointer
 */
