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
