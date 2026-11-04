class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Brute Force approach
# Tags: two-pointer
