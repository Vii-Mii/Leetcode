class Solution:
    def maxArea(self, height: list[int]) -> int:

        #Brute-froce approach
        # most_water = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         water = min(height[i],height[j]) * (j-i)
        #         most_water = max(water,most_water)
        # return most_water

        #optimal approach
        most_water = 0
        left = 0
        right = len(height)-1

        while left < right:
            calculate_water = min(height[left],height[right]) * (right-left)
            most_water = max(most_water,calculate_water)

            print(left,right, calculate_water, most_water)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return most_water

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Optimised solution using the two pointer converging approach
# Tags: two-pointer
