class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if not stack1 and i == '#':
                continue
            elif i != "#":
                stack1.append(i)
            else:
                stack1.pop()

        for j in t:
            if not stack2 and j == '#':
                continue
            elif j != "#":
                stack2.append(j)
            else:
                stack2.pop()

        return stack1 == stack2

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Used stack
# Tags: stack
