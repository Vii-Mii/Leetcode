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
