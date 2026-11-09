class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        if len(arr) == 1:
            return [-1]
        arr.append(-1)
        max_right = arr[len(arr)-2]
        
        for i in range(len(arr)-2,0,-1):
            if arr[i] <= max_right:
                arr[i] = max_right
            else:
                max_right = arr[i]
                continue
        return arr[1:]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Inplace array modification
# Tags: brute-force

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            max_value = max(right_max, arr[i])
            arr[i] = right_max
            right_max = max_value
        return arr

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimized approach
# Tags: brute-force
