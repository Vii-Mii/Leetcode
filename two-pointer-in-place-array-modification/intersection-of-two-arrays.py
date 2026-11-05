class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        values = set(nums1)
        result = set()
        for i in nums2:
            if i in values:
                result.add(i)
        return list(result)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Brute force
#     Set approach
# Tags: hashing

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        result = []
        left, right = 0,0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                if not result or result[-1] != nums1[left]:
                    result.append(nums1[left])
                left += 1
                right += 1

        return result

# Time Complexity: O(log n)
# Space Complexity: O(n)
# Approach: Two pointer traversing each array
# Tags: two-pointer
