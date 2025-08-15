from typing import List, Dict, Any

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        LeetCode 212: Word Search II
        1) Build a Trie (prefix tree) from the given word list.
        2) Start DFS + backtracking from each board cell, walking in sync with the Trie.
        3) If we reach a Trie node with WORD_KEY, we've found a complete word.
        """
        WORD_KEY = "$"  # Special marker in the Trie for "this is the end of a word"

        # ---------------------------------------------------------------------
        # 1. Build the Trie (nested dict). Each key is a letter, each value is a child node (dict).
        # ---------------------------------------------------------------------
        trie: Dict[str, Any] = {}
        for word in words:
            node = trie
            for letter in word:
                # setdefault(key, default):
                # - If key exists, return node[key]
                # - If key does not exist, set node[key] = default and return default
                # This is equivalent to:
                # if letter not in node: node[letter] = {}
                # node = node[letter]
                node = node.setdefault(letter, {})
            # Mark the complete word at the final node using a special key
            node[WORD_KEY] = word

        rowNum, colNum = len(board), len(board[0])
        matchedWords: List[str] = []

        # ---------------------------------------------------------------------
        # 2. Backtracking (DFS)
        # backtracking(row, col, parent):
        # - row, col: current position on the board
        # - parent: the current Trie node (dict) for the prefix we've matched so far
        #   Using `parent` lets us continue from the current prefix instead of starting from the root.
        # ---------------------------------------------------------------------
        def backtracking(row: int, col: int, parent: Dict[str, Any]) -> None:
            letter = board[row][col]
            currNode = parent[letter]  # Move into the Trie for (prefix + current letter)

            # 1) Check if we found a complete word
            # pop(WORD_KEY, False):
            #   - If present: returns the word and removes it from the Trie node
            #     (avoids duplicates in matchedWords)
            #   - If absent: returns False
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)

            # 2) Mark this cell as visited so it can't be used twice in the same path
            # We temporarily overwrite it with "#" and restore it later.
            board[row][col] = "#"

            # 3) Explore neighbors in four directions: up, right, down, left
            for d_row, d_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = row + d_row, col + d_col

                # Skip out-of-bounds positions
                if nr < 0 or nr >= rowNum or nc < 0 or nc >= colNum:
                    continue

                # Skip if the next letter is not a child of the current Trie node
                nxt = board[nr][nc]
                if nxt not in currNode:
                    continue

                # Recurse into the next cell
                backtracking(nr, nc, currNode)

            # 4) Restore the cell's letter after exploration
            board[row][col] = letter

            # 5) Trie pruning (optimization):
            # If the current node has no children left, remove it from its parent.
            # This shortens the search for future paths.
            if not currNode:
                parent.pop(letter)

        # Start backtracking from any cell whose letter is in the Trie root
        for r in range(rowNum):
            for c in range(colNum):
                if board[r][c] in trie:
                    backtracking(r, c, trie)

        return matchedWords
