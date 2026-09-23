class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur_board = [["." for i in range(n)] for i in range(n)]
        
        # ... i was very proud of my upgrade grid approach
        # but yes it was o(n^2)
        # apparently we got a math property to help us check
        # diags much more easily:
        # in diag top left to bot right, r - c is constant
        # in diag top right to bot left, r + c is constant
        # we just need three sets.

        used_cols = set()
        used_major_diags = set()
        used_minor_diags = set()
        
        def add_queen(row, col):
            cur_board[row][col] = "Q"
            used_cols.add(col)
            used_major_diags.add(row - col)
            used_minor_diags.add(row + col)
        
        def remove_queen(row, col):
            cur_board[row][col] = "."
            used_cols.remove(col)
            used_major_diags.remove(row - col)
            used_minor_diags.remove(row + col)
        
        def is_valid_queen_pos(row, col):
            if (
                col in used_cols or
                row - col in used_major_diags or
                row + col in used_minor_diags
            ):
                return False
            return True

        def register_solution():
            solution = []
            for row in cur_board:
                solution.append("".join(row))
            res.append(solution)

        def backtrack(q_left, r):
            if q_left == 0:
                register_solution()
                return
            if r >= n:
                return

            for c in range(n):
                if not is_valid_queen_pos(r, c):
                    continue
                add_queen(r, c)
                backtrack(q_left - 1, r + 1)
                remove_queen(r, c)
        
        backtrack(n, 0)
        return res