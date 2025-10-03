from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # build a array of length = amount+1，intialized as amount+1 >> ∞
        dp = [amount + 1] * (amount + 1)

        # base: we need 0 coin to get the amount of 0
        dp[0] = 0

        # calculate the min coins needed to accumulate amount a
        for a in range(1, amount + 1):
            # try every coin
            for c in coins:
                # only when a-c >= 0（which means we can use this coin, update
                if a - c >= 0:
                    # The best answer
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If in the end, dp[amount] still equals to the initial value, it means that we cannot reach the amount; or return the best solution
        return dp[amount] if dp[amount] != amount + 1 else -1
