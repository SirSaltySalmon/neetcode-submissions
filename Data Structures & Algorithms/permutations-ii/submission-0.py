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
                    pCopy.insert(j, nums[i])
                    if not tuple(pCopy) in existing:
                        existing.add(tuple(pCopy))
                        res.append(pCopy)
            return res
        
        return permuteOfNumbersFromIndex(0)