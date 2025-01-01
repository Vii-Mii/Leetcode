class Solution:
    def maxScore(self, s: str) -> int:
        max_value = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            max_value = max(max_value,left.count("0")+right.count("1"))
            print(left,right)
        return max_value


# TC : O(n2)
# SC : O(1)