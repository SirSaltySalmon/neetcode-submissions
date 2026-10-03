class Solution:
    def jump(self, nums: List[int]) -> int:
        # we wanna go as far as we can each jump
        # so at our index find the next one we can reach
        # that takes us the furthest as possible
        # how to optimize?
        
        count = 0
        i = 0
        while True:
            if i == len(nums) - 1:
                return count
            if nums[i] + i >= len(nums) - 1:
                return count + 1
            reachable = range(i, nums[i] + i + 1)
            furthest_possible = (0, 0)
            for index in reachable:
                furthest_possible = max((index + nums[index], index), furthest_possible)
            i = furthest_possible[1]
            count += 1
        return count