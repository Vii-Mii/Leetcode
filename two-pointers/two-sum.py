class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, optimized

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

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
#new version 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, optimized
