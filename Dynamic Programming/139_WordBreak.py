class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        # s =    leetcode
        # dp = T FFFFFFFF

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        # when i = 4, start = 4 - 4 ("leet") = 0 >> T
        # so fulfill if-condition (start = 0, dp[start] = True, s[0:4] == "leet") 
        # >> dp[4] = T 
        # now: s =    leetcode
        #      dp = T FFFTFFFF


        return dp[-1]
