class Solution:
    def climbStairs(self, n: int) -> int:
        # well...... let's think of this recursively
        # one way to climb 1 step
        # 2 ways to climb 2 step
        # 3 steps? ways to climb 2 then add 1, and ways to climb 1 then add 2
        # 4 steps? ways to climb 3 then add 1, and ways to climb 2 then add 2...
        # we get the idea
        # so at most we only need 2 memory space to store 2 previouses
        # let's use dp and bottoms up
        # for o(n) time and o(1) space

        last_2_steps = [1, 2]
        if n <= 2:
            return last_2_steps[n - 1]
        
        res = last_2_steps[1]
        for i in range(2, n):
            res = last_2_steps[0] + last_2_steps[1]
            last_2_steps[0] = last_2_steps[1]
            last_2_steps[1] = res
        return res