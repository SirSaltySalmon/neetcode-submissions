import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # no need to square root, just square
        # as only considering comparative distance
        distances = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            distances.append((dist, point))
        
        heapq.heapify(distances)
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        
        return res