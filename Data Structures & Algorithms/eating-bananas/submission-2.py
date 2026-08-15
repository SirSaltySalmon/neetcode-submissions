import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition:
        # Minimum number of hours is achieved by eating all bananas in a pile in one hour
        # Maximum number of hours is achieved by totaling up the amount in piles, k = 1
        # Lower bound is sum(piles) / h
        # binary search?

        bot_k = math.ceil(sum(piles) / h)
        top_k = max(piles)

        def can_eat_bananas(k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            return time <= h
        
        while bot_k < top_k:
            mid = (bot_k + top_k) // 2
            if can_eat_bananas(mid):
                top_k = mid
            else:
                bot_k = mid + 1
        
        return bot_k
