import heapq

class KthLargest:
    k: int
    max_heap: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for i in range(len(nums)):
            nums[i] = -nums[i]
        self.max_heap = nums
        heapq.heapify(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)

        heap_copy = self.max_heap.copy()
        res = -heap_copy[0]
        for i in range(self.k):
            res = -heapq.heappop(heap_copy)
        
        return res