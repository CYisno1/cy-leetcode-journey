from functools import lru_cache
# @lru_cache: 將每次遞迴呼叫的結果記錄下來，
# 若之後以相同參數呼叫，直接回傳快取值以節省重複運算。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2): # memo_solve(p1, p2): 代表從 text1[p1:] 和 text2[p2:] 開始的 LCS 長度
            if p1 == len(text1) or p2 == len(text2): 
                return 0
            # 任一字串到尾巴時，沒有字可比，LCS 長度是 0
            
            # Recursive case 1
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            
            # Recursive case 2
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
        
        return memo_solve(0, 0)
