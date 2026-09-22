class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permuteOfNumbersFromIndex(i):
            if i >= len(nums):
                return [[]]
            
            res = []
            perms = permuteOfNumbersFromIndex(i+1)
            for p in perms:
                # +1 because u want before, all in betweens, and after
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        
        return permuteOfNumbersFromIndex(0)