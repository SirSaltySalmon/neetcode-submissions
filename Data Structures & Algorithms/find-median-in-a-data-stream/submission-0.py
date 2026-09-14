import heapq

class MedianFinder:
    small: list
    large: list

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # add to small by default.
        heapq.heappush(self.small, -num)
        # then, if:
        # max of small > min of large => pop from small, move to large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # then handle uneven size, for:
        # len(small) > len(large) + 1 => pop from small, move to large
        # len(large) > len(small) + 1 => pop from large, move to small
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            res = (-self.small[0] + self.large[0]) / 2
            return res
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]