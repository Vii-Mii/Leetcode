from typing import List

def check(self, nums: List[int]) -> bool:
    sort_nums = sorted(nums)
    for i in range(len(nums)):
        if nums == sort_nums:
            return True
        nums.append(nums.pop(0))
    return False

# Time complexity : O(n2*logn) takes n for the iteration and nlogn for the sorting the array
# Space complexity : O(n) take a space for the sorted array and nums itself since modifying the value within the array

def check(self, nums: List[int]) -> bool:
    breaks = 0
    for i in range(len(nums)):
        if nums[i] < nums[i - 1]:
            breaks += 1
    return True if breaks <= 1 else False

# Time complexity : O(n) single iteration (logic is if the array sorted & rotated there is at least one break point)
# Space complexity : O(1) since not using any space