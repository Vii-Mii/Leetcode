class Solution:
    def sortedSquares(self, arr: list[int]) -> list[int]:
        left = 0
        right = len(arr)-1
        index = len(arr)-1
        res = [0]*len(arr)

        while left <= right:
            if abs(arr[left]) > abs(arr[right]):
                res[index] = arr[left]**2
                left += 1
            else:
                res[index] = arr[right]**2
                right -= 1
            index -= 1
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, binary-search, optimized
