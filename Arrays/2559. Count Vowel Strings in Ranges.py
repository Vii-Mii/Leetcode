from collections import defaultdict
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        pre_sum = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                pre_sum[i + 1] = pre_sum[i] + 1
            else:
                pre_sum[i + 1] = pre_sum[i]
        result = []
        for start, end in queries:
            result.append(pre_sum[end + 1] - pre_sum[start])

        return result

#
# Time Complexity : O(m) + O(n)
# Space Complexity : O(n)