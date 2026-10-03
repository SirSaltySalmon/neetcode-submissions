class Solution:
    def jump(self, nums: List[int]) -> int:
        # we wanna go as far as we can each jump
        # so at our index find the next one we can reach
        # that takes us the furthest as possible
        # how to optimize?
        
        count = 0
        i = 0
        while True:
            if i >= len(nums) - 1:
                return count
            if i + nums[i] >= len(nums) - 1:
                return count + 1
            reachable = range(i + 1, min(i + nums[i] + 1, len(nums)))

            furthest_possible = (0, 0)
            for index in reachable:
                furthest_possible = max((index + nums[index], index), furthest_possible)
            i = furthest_possible[0]
            count += 2
        
        return count