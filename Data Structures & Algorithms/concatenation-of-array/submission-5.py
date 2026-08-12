class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        for j in range(len(nums)):
            ans[j] = nums[j]
            ans[j + len(nums)] = nums[j]
        return ans