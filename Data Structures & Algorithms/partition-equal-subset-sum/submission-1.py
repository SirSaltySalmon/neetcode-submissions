class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        diff = 0
        memo = set()

        def backtracking(i):
            nonlocal diff
            # print(i, diff)
            if (i, diff) in memo:
                return False
            if i == len(nums):
                if diff == 0:
                    return True
                else:
                    memo.add((i, diff))
                    return False
            # add cur num to partition 1
            diff += nums[i]
            if backtracking(i + 1):
                return True
            # add cur num to partition 2
            memo.add((i + 1, diff))
            diff -= (nums[i] * 2)
            if backtracking(i + 1):
                return True
            memo.add((i + 1, diff))
            diff += nums[i]
            return False
        
        return backtracking(0)