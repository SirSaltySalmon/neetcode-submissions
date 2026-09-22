class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        res = []
        cur = []

        def backtrack(start, remain):
            if remain == 0:
                res.append(list(cur))
                return
            for j in range(start, len(nums)):
                if nums[j] > remain:
                    break  # Prune since array is sorted
                if j > start and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate elements at the same depth
                cur.append(nums[j])
                backtrack(j + 1, remain - nums[j])
                cur.pop()
        
        backtrack(0, target)
        return res