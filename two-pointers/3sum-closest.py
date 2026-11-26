class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = float(inf)
        res = 0 

        for left in range(len(nums)-2):
            mid = left + 1
            right = len(nums)-1

            while mid < right:
                val = nums[left] + nums[mid] + nums[right]
                if val == target:
                    return val
                elif val > target:
                    closest = abs(target-val)
                    if closest < diff:
                        diff = closest
                        res = val
                    right -= 1
                else:
                    closest = abs(target-val)
                    if closest < diff:
                        diff = closest
                        res = val
                    mid += 1
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, optimized
