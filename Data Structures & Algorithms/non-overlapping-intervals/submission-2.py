class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[0])

        def overlaps(i1, i2):
            return intervals[i1][1] > intervals[i2][0]
        
        # approach: when two overlaps,
        # remove one OR the other
        # which should we keep?
        # well the one that ends earlier. then it is less likely to overlap

        def dfs(prev_i, cur_i, removed):
            if cur_i == len(intervals):
                return removed
            if overlaps(prev_i, cur_i):
                if intervals[prev_i][1] < intervals[cur_i][1]:
                    return dfs(prev_i, cur_i + 1, removed + 1)
                return dfs(cur_i, cur_i + 1, removed + 1)
            return dfs(cur_i, cur_i + 1, removed)
        
        i = 1
        last_i = 0
        removed = 0
        while i < len(intervals):
            if overlaps(last_i, i):
                removed += 1
                if intervals[last_i][1] > intervals[i][1]:
                    last_i = i
            else:
                last_i = i
            i += 1
        return removed