"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        
        # we want to log end dates
        # once a meeting ends the room frees up
        # let's use a queue
        # a queue doesnt work cause we dont guarantee earliest finish is on top
        # some sort of data structure where min is always accessible...
        # that's a heap!
        room_count = 0
        heap = []
        for i in range(len(intervals)):
            cur_time = intervals[i].start
            while heap and heap[0] <= cur_time:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            room_count = max(room_count, len(heap))
        
        return room_count