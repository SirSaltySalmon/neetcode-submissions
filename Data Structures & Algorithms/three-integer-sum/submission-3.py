class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #It is not just TwoSum.
        nums.sort()
        results = []

        for i in range(0, len(nums)-1):
            if nums[i] > 0:
                break
            
            # Skip duplicates for first number!!!
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            start_i = i + 1
            end_i = len(nums) - 1

            while start_i < end_i:
                twosum = nums[start_i] + nums[end_i]
                if twosum > target:
                    end_i -= 1
                elif twosum < target:
                    start_i += 1
                else:
                    answer = [nums[i], nums[start_i], nums[end_i]]
                    results.append(answer)
                    start_i += 1
                    end_i -= 1
                    while nums[start_i] == nums[start_i - 1] and start_i < end_i:
                        start_i += 1
        
        return results



        