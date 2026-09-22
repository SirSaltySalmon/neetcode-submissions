class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        
        def permuteOfNumbersFromIndex(i):
            if i >= len(nums):
                return [[]]
            
            existing = set()

            res = []
            perms = permuteOfNumbersFromIndex(i+1)
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    if j > 0 and p[j-1] == nums[i]:
                        break
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        
        return permuteOfNumbersFromIndex(0)