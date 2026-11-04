class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = {}
        nums.sort()
        for left in range(len(nums)):
            mid = left + 1
            right = len(nums)-1 

            while mid < right:
                val = nums[left] + nums[mid] + nums[right]
                if val > target:
                    closest[abs(target - val)] = val
                    right -= 1
                else: 
                    closest[abs(target - val)] = val
                    mid += 1
        print(closest)
        return closest[min(closest.keys())]

/*
 * Time Complexity: O(n²)
 * Space Complexity: O(n²)
 * Approach: two pointer
 *     hash
 * Tags: two-pointer
 */
