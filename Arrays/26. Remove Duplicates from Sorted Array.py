from typing import List

def removeDuplicates(self, arr: List[int]) -> int:
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    for i in range(len(unique)):
        arr[i] = unique[i]
    return len(unique)

# Time complexity : O(n2)
# Space complexity : O(n)

def removeDuplicates(self, arr: List[int]) -> int:
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    return i + 1

# Time complexity : O(n)
# Space complexity : O(1)