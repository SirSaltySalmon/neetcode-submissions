class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set(nums)
        if len(table) < len(nums):
            return True
        return False