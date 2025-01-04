class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        for i in range(1, len(s) - 1):
            left_set = set()
            right_set = set(s[i + 1:])

            for j in range(i):
                left_set.add(s[j])

            for j in left_set:
                if j in right_set:
                    result.add((j, s[i], j))
        return len(result)

# Time Complexity : O(n2)
# Space Complexity : O(n)