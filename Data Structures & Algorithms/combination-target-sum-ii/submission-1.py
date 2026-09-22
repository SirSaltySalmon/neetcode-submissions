class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        cur = []
        
        # main issue: same total, same num => duplicated result.
        # approach 1: use hashset to check?
        # approach 2: at the exclude step, skip to next i that isn't the same
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums):
                return
            if total + nums[i] > target:
                return
            
            #1. include
            cur.append(nums[i])
            dfs(i + 1, total + nums[i])
            #2. exclude
            cur.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res