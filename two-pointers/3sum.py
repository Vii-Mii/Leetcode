class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result = set()
        for left in range(len(arr)-2):
            mid = left + 1
            right = len(arr)-1

            while mid < right:
                val = arr[left] + arr[mid] + arr[right]
                if val == 0:
                    result.add(tuple([arr[left],arr[mid],arr[right]]))
                    mid += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    mid += 1
        return [list(i) for i in result]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two Pointers technique traversing from boundaries inward to find matching conditions in linear time.
# Tags: two-pointer, optimized
