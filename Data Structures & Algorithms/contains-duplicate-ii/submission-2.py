class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        R = 0
        hashmap = {}
        while R < len(nums):
            if R - L > k:
                L += 1
            if nums[R] in hashmap:
                if hashmap[nums[R]] >= L:
                    return True
            hashmap[nums[R]] = R
            R += 1
        return False