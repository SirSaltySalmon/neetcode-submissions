import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first_stone = heapq.heappop(stones) * -1
            second_stone = heapq.heappop(stones) * -1
            if first_stone != second_stone:
                heapq.heappush(stones, abs(first_stone - second_stone) * -1)
        
        return 0 if not stones else stones[0] * -1