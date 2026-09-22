class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # so i think our decision tree is...
        # smallest available starting num, try future combos...
        # then mix up with a larger starting num
        # all future nums are larger than previous
        # terminate? when starting num to end num would be
        # just consecutive numbers soooo
        # when num = n - k + 1
        # need to generalize for all positions!
        # num = n - k + len(cur) + 1

        res = []
        cur = []

        def dfs(num):
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            while num <= (n - k + len(cur) + 1):
                cur.append(num)
                num += 1
                dfs(num)
                cur.pop()
        
        dfs(1)
        return res