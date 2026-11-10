class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        queue = []
        max_length = 0
        for i in range(len(arr)):
            if not queue or len(queue) == 1:
                if len(queue) == 1 and queue[-1] == arr[i]:
                    continue
                queue.append(arr[i])
            elif (queue[-2] > queue[-1] < arr[i]) or (queue[-2] < queue[-1] > arr[i]):
                queue.append(arr[i])
            else:
                queue = [queue[-1]]
                if queue[-1] != arr[i]:
                    queue.append(arr[i])
            max_length = max(max_length, len(queue))
        return max_length

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Kadane's algorithm
# Tags: kadane
