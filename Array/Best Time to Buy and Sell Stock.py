"""
To get the max profit, we have to buy in at the lowest price and sell when current price - buy_price is max. We iterate through the prices array from index 1 and update the lowest buy_price.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)

        return profit
        
