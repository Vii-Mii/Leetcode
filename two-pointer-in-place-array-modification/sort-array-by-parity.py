class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0 
        right = len(nums)-1

        while left <= right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 == 0 and nums[right] % 2 == 0:
                left += 1
            elif nums[left] % 2 == 0 and nums[right] % 2 != 0:
                left += 1
                right -= 1
            elif nums[left] % 2 != 0 and nums[right] % 2 != 0:
                right -= 1

        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Brute force approach
#     arranging the even & odd by condition
# Tags: two-pointer

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0 
        right = len(nums)-1

        while left <= right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two pointer
#     with minimal condiition
# Tags: two-pointer

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimized single for loop approach
# Tags: two-pointer, optimized
