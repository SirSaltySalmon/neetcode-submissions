class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this is cycle detection.
        # how did I not realize?
        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # initialize new slow
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow