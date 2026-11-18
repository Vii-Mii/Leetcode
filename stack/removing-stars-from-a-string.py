class Solution:
    def removeStars(self, s: str) -> str:

        s = list(s)
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return 
        return "".join(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Monotonic Stack / LIFO tracking to process matching boundaries and maintain ordered candidates.
# Tags: stack, optimized
