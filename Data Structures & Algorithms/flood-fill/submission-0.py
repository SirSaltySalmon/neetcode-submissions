class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_col = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if min(r,c) < 0 or r >= len(image) or c >= len(image[r]):
                return
            if image[r][c] != starting_col:
                return
            if (r,c) in visited:
                return

            image[r][c] = color
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        
        dfs(sr, sc)
        return image