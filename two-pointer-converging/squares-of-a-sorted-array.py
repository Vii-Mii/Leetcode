class Solution:
    def sortedSquares(self, arr: list[int]) -> list[int]:
        left = 0
        right = len(arr)-1
        result = [0]*len(arr)
        index = len(arr)-1

        while left <= right:
            if abs(arr[left]) > abs(arr[right]):
                result[index] = arr[left] ** 2
                left += 1
            else:
                result[index] = arr[right] ** 2
                right -= 1
            index -= 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Two Pointer (Converging)
# Tags: two-pointer
