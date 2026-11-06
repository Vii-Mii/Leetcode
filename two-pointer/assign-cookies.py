class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        left = 0
        right = 0

        count = 0

        while right < len(s) and left < len(g):
            if s[right] >= g[left]:
                right += 1
                left += 1
                count += 1
            else:
                right += 1

        return count

# Tags: two-pointer, greedy
