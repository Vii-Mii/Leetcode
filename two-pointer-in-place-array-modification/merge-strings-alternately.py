class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        left,right = 0,0

        while left < len(word1) and right < len(word2):
            result += word1[left]
            result += word2[right]
            left += 1
            right += 1
        
        print(result,left,right)
        
        while left < len(word1):
            result += word1[left]
            left += 1
        print(result,left,right)
        
        while right < len(word2):
            result += word2[right]
            right += 1
        print(result,left,right)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Brute Force approach
#     Use while loop to fill the non append string not the if
# Tags: two-pointer, brute-force
