class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        values = {}
        for i in range(len(arr)):
            val = target - arr[i]
            if val in values:
                return [values[val]+1,i+1]
            else:
                values[arr[i]] = i

        return [1,1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hashing
#     Brute force approach
# Tags: hashing

// --------------------------------------------------------------------------------
// Next Solution Version
// --------------------------------------------------------------------------------

class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        left = 0
        right = len(arr)-1

        while left < right:
            if arr[left] + arr[right] == target:
                return [left+1,right+1]
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1

        return [1,1]

/*
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Approach: Two pointer (Converging)
 * Tags: two-pointer
 */
