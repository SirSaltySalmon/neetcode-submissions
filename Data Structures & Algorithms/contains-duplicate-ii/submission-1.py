class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        R = 0
        while R < len(nums):
            if R - L > k:
                L += 1
            if len(set(nums[L:R+1])) < len(nums[L:R+1]):
                return True
            R += 1
        return False