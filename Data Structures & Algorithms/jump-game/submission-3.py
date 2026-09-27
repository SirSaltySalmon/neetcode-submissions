class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # so... this can be done really easy actually
        # theres no specific requirement on landing DIRECTLY
        # on anything.
        # the easier way is just to track the furthest
        # you can go at all time.
        # you always return False early correctly,
        # as terminates when you go to a tile that would
        # be able to jump to destination, but cannot
        # be reached itself.
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True
        return True