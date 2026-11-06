class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            column = []
            for j in range(len(matrix)):
                column.append(matrix[j][i])
            transpose.append(column)
        return transpose

# Time Complexity: O(n²)
# Space Complexity: O(n²)
# Tags: two-pointer
