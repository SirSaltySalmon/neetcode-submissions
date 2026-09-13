import heapq
from collections import deque

# VERY IMPORTANT OPTIMIZATION.
# I honestly should've thought of this.
# I am storing cd and ticking them down every cycle.
# But this is costly as I need to iterate every cycle.
# My approach already works because I've guaranteed
# that each task in cd queue has an unique eviction time.
# Why not apply this to just checking if eviction time is met?

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        initial_freq = {}
        for task in tasks:
            freq = initial_freq.get(task, 0) + 1
            initial_freq[task] = freq
        
        # keep track of most frequent task in max heap to do first
        # whenever available, always
        max_heap = []
        for i, (k, v) in enumerate(initial_freq.items()):
            heapq.heappush(max_heap, [v * -1, k])
        
        res = 0
        cd_queue = deque()
        while max_heap or cd_queue:
            res += 1
                        
            if cd_queue and cd_queue[0][0] == res:
                cooled_down_task_data = cd_queue.popleft()[1]
                if cooled_down_task_data[0] < 0:
                    heapq.heappush(max_heap, cooled_down_task_data)

            if max_heap:
                next_task_data = heapq.heappop(max_heap)
                next_task_data[0] += 1
                if next_task_data[0] != 0:
                    # mark the time for it to be evicted
                    cd_queue.append([res + n + 1, next_task_data])
                    
        return res