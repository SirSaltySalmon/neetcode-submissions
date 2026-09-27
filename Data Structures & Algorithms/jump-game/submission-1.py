class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force, O(n^2), works but exceed time limit
        # how do I make this O(n)

        dead_end = set()

        def jump(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            if i in dead_end:
                return False
            
            max_jumps = nums[i]
            for x in range(max_jumps, 0, -1):
                if jump(i+x):
                    return True
            dead_end.add(i)
            return False
        
        return jump(0)