class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result = set()

        for left in range(len(arr)-2):
            mid = left + 1
            right = len(arr)-1 

            while (mid < right):
                val = arr[left] + arr[mid] + arr[right]
                if val == 0:
                    result.add(tuple(sorted([arr[left],arr[mid],arr[right]])))
                    mid += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    mid += 1
            
        return [list(i) for i in result]

# Time Complexity: O(n²)
# Space Complexity: O(n)
# Approach: Two pointer (converging)
#     with set
# Tags: two-pointer

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result = []

        for left in range(len(arr)-2):
            mid = left + 1
            right = len(arr)-1 

            if left > 0 and arr[left] == arr[left-1]:
                continue

            while (mid < right):
                val = arr[left] + arr[mid] + arr[right]
                if val == 0:
                    result.append([arr[left],arr[mid],arr[right]])
                    mid += 1
                    right -= 1

                    while mid < right and arr[mid] == arr[mid-1]:
                        mid += 1
                    while mid < right and arr[right] == arr[right+1]:
                        right -= 1
                elif val > 0:
                    right -= 1
                else:
                    mid += 1
            
        return result

# Time Complexity: O(n²)
# Space Complexity: O(n)
# Approach: Two pointer (Converging)
#     Without set & Duplicates
# Tags: two-pointer
