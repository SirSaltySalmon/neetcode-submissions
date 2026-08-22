class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                max_profit = max(prices[R] - prices[L], max_profit)
        return max_profit
