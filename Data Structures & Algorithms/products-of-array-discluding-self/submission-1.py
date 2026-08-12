class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = nums.copy()
        for i in range(1, len(nums), 1):
            prefix_products[i] = prefix_products[i-1] * nums[i]

        suffix_products = nums.copy()
        for i in range(len(nums)-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i]
        
        results = [0 for i in range(len(nums))]
        results[0] = suffix_products[1]
        results[len(nums)-1] = prefix_products[len(nums)-2]
        for i in range(1, len(nums)-1, 1):
            results[i] = prefix_products[i-1] * suffix_products[i+1]

        return results        
