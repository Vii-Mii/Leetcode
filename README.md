# LeetCode

Python solutions to LeetCode problems, grouped by technique.

Built as daily practice for problem-solving and data structures and algorithms.

## Structure

```
.
├── two-pointer-converging/   # problems grouped by technique
├── array-manipulation                 
└── stack-queue                
```

- One solution per file, named after the problem in lowercase with hyphens (`two-sum.py`).
- Problems that share a technique live together in a folder named after it.

## Topics

Arrays · Strings · Linked lists · Trees · Graphs · Dynamic programming

## Solution template

Each file can follow the same short shape:

```python
"""
Two Sum · Easy
https://leetcode.com/problems/two-sum/

Approach: hash map of value -> index, one pass.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
```

## Author

[Vii-Mii](https://github.com/Vii-Mii)