class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's for max subarray
        max_sum = nums[0]
        cur_max = 0
        # Kadane's for min subarray
        min_sum = nums[0]
        cur_min = 0
        total = 0
        
        for x in nums:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
            total += x
            
        # If all numbers are negative, max_sum is the answer
        if max_sum < 0:
            return max_sum
            
        # Return max of normal Kadane and circular (total - min)
        return max(max_sum, total - min_sum)