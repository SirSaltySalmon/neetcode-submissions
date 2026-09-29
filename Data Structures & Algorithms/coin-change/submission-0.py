from abc import abstractmethod
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute force approach
        # select from largest amount
        # then start selecting smaller
        # fails then try again
        # obviously this sucks if done by itself
        # but i can imagine the target getting smaller and smaller
        # memoizable results

        memo = {}
        
        def min_coins(amount_left):
            if amount_left < 0:
                return float("inf")
            if amount_left == 0:
                return 0
            if amount_left in memo:
                return memo[amount_left]
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1 + min_coins(amount_left - coin))
            memo[amount_left] = res
            return res
        
        ans = min_coins(amount)
        if ans != float("inf"):
            return ans
        return -1
                