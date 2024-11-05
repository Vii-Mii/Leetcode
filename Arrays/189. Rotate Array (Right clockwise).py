from typing import List

def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# for the right clockwise reverse the whole array first and then reverse the parts
# for the left clockwise reverse the parts first and then the whole array
def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[0:k] = nums[0:k][::-1]
    nums[k:len(nums)] = nums[k:len(nums)][::-1]

# Time complexity : O(n)
# Space complexity : O(1)

