"""
For clockwise 90 degrees rotation: Transpose -> Reverse
counter clockwise: Reverse -> Transpose

Original matrix A:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

After Transpose:
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

After Reverse:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse the list (each row)
        for row in matrix:
            row.reverse()
