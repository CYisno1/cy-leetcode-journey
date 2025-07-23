"""
In the backtracking- recursion part:
Each level of backtracking only handles the current character it is responsible for: suffix[0].
The next recursive call continues searching for the remaining part of the word: suffix[1:].
When suffix == "", it means the entire word has been successfully found, so the function returns True.

suffix represents the remaining substring that hasn’t been matched yet.
Each time we match one character, suffix moves one character forward.

| Backtrack Level  | Matched Char  | Current suffix | suffix[0] | suffix[1:] |
|------------------|---------------|----------------|-----------|-------------|
| Level 1          | D             | "DOG"          | "D"       | "OG"        |
| Level 2          | O             | "OG"           | "O"       | "G"         |
| Level 3          | G             | "G"            | "G"       | "" (empty)  |
| Level 4          | —             | "" (empty)     | —         | — → return True ✅ |

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        
        return False
    
    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True
        
        # Check the current status
        if (
            row < 0
            or row == self.ROWS
            or col < 0
            or col == self.COLS
            or self.board[row][col] != suffix[0]
        ):
            return False
        
        # Backtracking
        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = "#"
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break to cleanup
            if ret:
                break
        
        # revert the change, make the board back to its original state
        self.board[row][col] = suffix[0]

        # Finish trying all directions and didn't find any match
        return ret

