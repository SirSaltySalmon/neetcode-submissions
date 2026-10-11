class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_set = set()
        res = 0

        def find_island(r, c):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[r]):
                return
            if grid[r][c] == "0":
                return
            if (r, c) in land_set:
                return
            land_set.add((r, c))
            find_island(r + 1, c)
            find_island(r - 1, c)
            find_island(r, c + 1)
            find_island(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "0":
                    continue
                if (r, c) in land_set:
                    continue
                res += 1
                find_island(r, c)
        
        return res