class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_of_nums = set()
        for num in nums:
            if num in set_of_nums:
                return num
            set_of_nums.add(num)
        return nums[0]