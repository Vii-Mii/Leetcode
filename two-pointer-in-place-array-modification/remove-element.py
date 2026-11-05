class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Two pointer
# Tags: two-pointer

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0 
        right = len(nums)-1


        while left <= right:
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
            else:
                left += 1
        return left

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Two pointer 
#     left, right pointer 
#     filling the element removed to the right of the list
# Tags: two-pointer
