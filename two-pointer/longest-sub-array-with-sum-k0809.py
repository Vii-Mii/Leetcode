# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        max_length = 0
        preSum = {}
        summ = 0

        for i in range(len(arr)):
            summ += arr[i]

            if summ == k:
                max_length = max(max_length,i+1)

            rem = summ - k
            if rem in preSum:
                length = i - preSum[rem]
                max_length = max(length,max_length)

            if summ not in preSum:
                preSum[summ] = i 

        return max_length

# Time Complexity: O(n)
# Space Complexity: O(n)
# Tags: two-pointer
