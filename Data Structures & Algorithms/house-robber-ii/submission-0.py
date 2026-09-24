class Solution:
    def rob(self, nums: List[int]) -> int:
        # run the algorithm selecting the first house
        # if selected first house cannot select last house
        # run the algorithm again selecting second house
        # get max of both

        if len(nums) <= 2:
            return max(nums)
        
        # 1. select first house
        dp = [nums[0], nums[0]]
        cur_house = 2
        while cur_house < len(nums):
            if cur_house != len(nums) - 1:
                skip = dp[1]
                rob = dp[0] + nums[cur_house]

                dp[0] = dp[1]
                dp[1] = max(skip, rob)
            else:
                # dp1 is already skip
                pass
            cur_house += 1
        
        ans1 = dp[1]

        # 2. select second house
        dp = [0, nums[1]]
        cur_house = 2
        while cur_house < len(nums):
            # no check, permitted to get last house this time
            skip = dp[1]
            rob = dp[0] + nums[cur_house]

            dp[0] = dp[1]
            dp[1] = max(skip, rob)
            cur_house += 1
        
        ans2 = dp[1]

        return max(ans1, ans2)