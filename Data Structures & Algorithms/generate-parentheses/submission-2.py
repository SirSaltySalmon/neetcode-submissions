class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decision to make each parenthesis....
        # start a child parenthesis,
        # or close x numbers of previous parenthesis before starting?
        res = []
        cur = []

        def backtrack(no_open, no_left):
            nonlocal res
            nonlocal cur

            if no_left == 0:
                cur.append(")" * no_open)
                res.append("".join(cur))
                cur.pop()
                return
            
            cur.append("(")
            backtrack(no_open + 1, no_left - 1)
            cur.pop()
            
            if no_open > 0:
                cur.append(")")
                backtrack(no_open - 1, no_left)
                cur.pop()
        
        backtrack(0, n)
        return res