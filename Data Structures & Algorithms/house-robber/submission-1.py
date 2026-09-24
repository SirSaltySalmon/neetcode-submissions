class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can skip or rob a house
        # best is max of last house
        # or we can rob
        # best is max of second last house + cur house
        # the best of the two decides what we want
        # so yes my intuition was kinda correct thinking it was
        # similar to backtracking
        # but the problem is simpler than backtracking so u can actually
        # just use dp.

        max_of_first_two = max(nums[0:2])

        if len(nums) <= 2:
            return max_of_first_two
        
        dp = [nums[0], max_of_first_two]
        cur_house = 2
        while cur_house < len(nums):
            skip = dp[1]
            rob = dp[0] + nums[cur_house]

            dp[0] = dp[1]
            dp[1] = max(skip, rob)
            cur_house += 1
        
        return dp[1]