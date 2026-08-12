class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in nums_index_dict:
                return [nums_index_dict[target - num], i]
                #Because i is always the largest index being checked
            
            nums_index_dict[num] = i