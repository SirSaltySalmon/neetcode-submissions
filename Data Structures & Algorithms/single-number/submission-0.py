class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for n in nums:
            xor_num = xor_num ^ n
        return xor_num