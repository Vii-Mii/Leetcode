class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = set()

        for last_left in range(len(nums)-3):
            for left in range(last_left+1, len(nums)-2):
                right = left + 1
                last_right = len(nums)-1

                while right < last_right:
                    val = nums[last_left] + nums[left] + nums[right] + nums[last_right]
                    if val == target:
                        result.add(tuple(sorted([nums[last_left],nums[left],nums[right],nums[last_right]])))
                        right += 1
                        last_right -= 1

                    elif val > target:
                        last_right -= 1
                    else:
                        right += 1
        return [list(i) for i in result]

# Time Complexity: O(n³)
# Space Complexity: O(n)
# Approach: Two pointer (Converging)
#     Used set to store results
# Tags: two-pointer
