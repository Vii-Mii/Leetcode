from collections import defaultdict
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = defaultdict(int)
        for i in nums:
            numbers[i] += 1
        for i in range(len(nums)):
            if numbers[i]== 0:
                return i
        return len(nums)

    # TC : O(n), SC : O(n)

    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums)+1) //2 - sum(nums)

    # TC : O(n), SC : O(1)

    def missingNumber(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        for i in range(len(nums)):
            xor1 ^= i
            xor2 ^= nums[i]
        xor1 ^= len(nums)
        return xor1 ^ xor2

    # TC : O(n), SC : O(1)
