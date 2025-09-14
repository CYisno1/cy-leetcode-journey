"""
Because we cannot use extra space, so we cannot use two sets to record where is 0.
We use first cells of every columns and rows as flags to mark which cells will later become 0.

The first cell of row and column for the first row and first column is the same >> cell[0][0].
Hence, we use an additional variable, is_col, to tell us if the first column had been marked or not and the cell[0][0] would be used to tell the same for the first row.

First, we iterate through the matrix and mark the flags.
Then, we go through the rest of the matrix (except the first row and first column), and mark the cells as 0 according to the flags.
We check the matrix[0][0] to tell whether the first row needed to be 0.
We check the is_col to tell whether the first column needed to be 0.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]: # if matrix[i][0] == 0 or matrix[0][j] == 0
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
            
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
