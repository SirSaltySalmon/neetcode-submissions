class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums) * 2)]
        for j in range(len(nums)):
            ans[j] = nums[j]
            ans[j + len(nums)] = nums[j]
        return ans