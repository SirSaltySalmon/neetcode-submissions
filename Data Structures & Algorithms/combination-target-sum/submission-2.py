class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # idea: to get a sum, potential next number must be less or equal
        # to diff between current sum and target
        # so its kind of a brute force solution.
        # i use 1x of number, look for matches in the next ones.
        # kind of recursion, subarrays and new target as the diff
        # then i use 2x of number, 3x, etc.
        # until next number to be used is larger than local target
        # anyway to save on computation? i suppose we are repeating use of numbers
        # but they're for different target values
        nums = sorted(nums)
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, total + nums[j])
                cur.pop()
        
        dfs(0, 0)
        return res
