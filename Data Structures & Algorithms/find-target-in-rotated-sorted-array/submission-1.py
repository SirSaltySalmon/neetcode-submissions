class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
        
        min_i = l
        # Now should we search before, or after min_i?
        if target >= nums[min_i] and target <= nums[-1]:
            l = min_i
            r = len(nums) - 1
        else:
            l = 0
            r = min_i - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

        