class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at each time you have a decreasing order...
        # you can choose to delete first or second
        memo = {}

        def helper(i, prev_idx):
            if i == len(nums):
                return 0
            if (i, prev_idx) in memo:
                return memo[(i, prev_idx)]
            
            # option 1: skip nums[i]
            res = helper(i + 1, prev_idx)
            
            # option 2: include nums[i] but only if increasing
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                res = max(res, 1 + helper(i + 1, i))
            memo[(i, prev_idx)] = res
            return res
        
        return helper(0, -1)