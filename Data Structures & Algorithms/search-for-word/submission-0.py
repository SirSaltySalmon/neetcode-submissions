class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def backtrack(r, c, i):
            if min(r,c) < 0 or r >= len(board) or c >= len(board[r]):
                return False
            if (r,c) in visited:
                return False
            if board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            if i == len(word) - 1:
                return True
            top = backtrack(r+1, c, i+1)
            bottom = backtrack(r-1, c, i+1)
            left = backtrack(r, c-1, i+1)
            right = backtrack(r, c+1, i+1)
            visited.remove((r,c))
            return top or bottom or left or right
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False