from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique = defaultdict(int)
        intersection = []
        for i in nums1:
            unique[i] += 1
        for i in nums2:
            if i in unique and unique[i] > 0:
                intersection.append(i)
                unique[i] -= 1
        return intersection

# Time complexity : O(n+m)
# Space complexity : O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        temp = []
        i = 0
        j = 0
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] == nums2[j]:
                temp.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return temp

# Time complexity : O(n+m)
# Space complexity : O(n+m)

# we also do return set(a) & set(b)



