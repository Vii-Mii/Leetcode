class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose = []
        for col in range(len(matrix[0])):
            value = []
            for row in range(len(matrix)):
                value.append(matrix[row][col])
            transpose.append(value)
        return transpose