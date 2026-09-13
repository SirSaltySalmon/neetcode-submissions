import heapq

# this max heap approach is clever indeed
# avoids heap operations from being logn
# when you only have a heap of k, operations are only logk
# so that's great

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # no need to square root, just square
        # as only considering comparative distance
        max_heap_distances = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if len(max_heap_distances) < k:
                heapq.heappush(max_heap_distances, (dist * -1, point))
            else:
                heapq.heappushpop(max_heap_distances, (dist * -1, point))
        
        res = []
        for data in max_heap_distances:
            res.append(data[1])
        
        return res