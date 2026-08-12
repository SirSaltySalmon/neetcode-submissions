class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)
        if len(nums) > len(set_of_nums):
            return True
        return False