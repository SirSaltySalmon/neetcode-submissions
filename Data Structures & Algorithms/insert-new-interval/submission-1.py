class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # ok old solution was not very generalised
        # next time just think hard and then write
        # insert or merge? well the big idea is...
        # if merge use max mins
        res = []
        smaller_bound = -1
        larger_bound = len(intervals)
        start = newInterval[0]
        end = newInterval[1]
        for i in range(len(intervals)):
            # orrrrr
            # we find the smaller ones,
            # and the larger ones
            # if smaller and larger are not consecutive then overlap is in between those
            if intervals[i][1] < newInterval[0]:
                smaller_bound = max(i, smaller_bound)
            if newInterval[1] < intervals[i][0]:
                larger_bound = min(i, larger_bound)
        
        if smaller_bound + 1 == larger_bound:
            return intervals[:smaller_bound + 1] + [newInterval] + intervals[larger_bound:]
        
        # smaller bound + 1 up to larger_bound - 1 overlaps
        merged_start = min(newInterval[0], intervals[smaller_bound + 1][0])
        merged_end = max(newInterval[1], intervals[larger_bound - 1][1])
        return intervals[:smaller_bound + 1] + [[merged_start, merged_end]] + intervals[larger_bound:]