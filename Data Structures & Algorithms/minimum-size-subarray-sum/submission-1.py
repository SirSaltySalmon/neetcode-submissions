class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums = [nums[0]] * len(nums)
        L = 0
        min_length = 0
        if nums[0] >= target:
            return 1
        for R in range(1, len(nums)):
            prefix_sums[R] = nums[R] + prefix_sums[R-1]
            cur_sum = 0
            if L != 0:
                cur_sum = prefix_sums[R] - prefix_sums[L-1]
            else:
                cur_sum = prefix_sums[R]
            while cur_sum >= target:
                cur_length = R - L + 1
                min_length = min(min_length, cur_length) if min_length != 0 else cur_length
                L += 1
                cur_sum = prefix_sums[R] - prefix_sums[L-1]
        
        return min_length