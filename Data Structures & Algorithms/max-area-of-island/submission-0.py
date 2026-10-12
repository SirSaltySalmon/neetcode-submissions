class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        land_set = set()
        res = 0
        cur_size = 0

        def find_island(r, c):
            nonlocal cur_size
            nonlocal res

            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[r]):
                return
            if grid[r][c] == 0:
                return
            if (r, c) in land_set:
                return
            land_set.add((r, c))
            cur_size += 1
            res = max(res, cur_size)
            find_island(r + 1, c)
            find_island(r - 1, c)
            find_island(r, c + 1)
            find_island(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    continue
                if (r, c) in land_set:
                    continue
                cur_size = 0
                find_island(r, c)
        
        return res