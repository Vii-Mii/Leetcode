class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat = 0
        left = 0
        right = len(people)-1

        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                boat += 1
                left += 1
                right -= 1
            else:
                boat += 1
                right -= 1
        
        return boat

# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: Two pointer Converging approach : Squezzing the left & right pointer from both the ends
# Tags: two-pointer
