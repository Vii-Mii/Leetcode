class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        result = 0
        for left in range(len(nums)):
            mid = left + 1
            right = len(nums)-1 

            while mid < right:
                val = nums[left] + nums[mid] + nums[right]
                if val > target:
                    closest = abs(target-val)
                    if closest < diff:
                        diff = closest
                        result = val
                    right -= 1
                else: 
                    closest = abs(target-val)
                    if closest < diff:
                        diff = closest
                        result = val
                    mid += 1
        return result

# Time Complexity: O(n²)
# Space Complexity: O(n²)
# Approach: Two pointer Converging
# Tags: two-pointer
