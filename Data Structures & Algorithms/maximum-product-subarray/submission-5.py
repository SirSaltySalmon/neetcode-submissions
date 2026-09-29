class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        res = nums[0]

        for n in nums:
            # Store cur_max * n before cur_max is overwritten
            temp = cur_max * n
            cur_max = max(n, temp, cur_min * n)
            cur_min = min(n, temp, cur_min * n)
            res = max(res, cur_max)
        
        return res