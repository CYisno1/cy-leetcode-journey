"""
There are two moving patterns: right + down and left + up
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Initialize possible number of steps
        direction = 1 # Start from going right
        i, j = 0, -1
        output = []

        while m * n > 0:

            # Move horizontally
            for _ in range(n):
                j += direction
                output.append(matrix[i][j])
            m -= 1
            
            # Move vertically
            for _ in range(m):
                i += direction
                output.append(matrix[i][j])
            n -= 1

            direction *= -1 # Flip direction
        
        return output
            

