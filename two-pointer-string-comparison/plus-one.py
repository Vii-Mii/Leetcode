class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        value = "".join([str(i) for i in digits])
        value = int(value)
        value += 1
        return [int(i) for i in str(value)]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Brute Force Approach
# Tags: brute-force
