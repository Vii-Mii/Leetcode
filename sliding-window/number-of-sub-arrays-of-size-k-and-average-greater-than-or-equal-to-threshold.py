class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = 0
        l = 0
        count = 0
        for r in range(len(arr)):
            window_sum += arr[r]
            
            if r-l+1 == k:
                if window_sum // k >= threshold:
                    count += 1
                window_sum -= arr[l]
                l += 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Sliding window
# Tags: sliding-window
