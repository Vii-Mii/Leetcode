class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Validating j to i-2 or i < 2
#     revisis
# Tags: two-pointer, revisit
