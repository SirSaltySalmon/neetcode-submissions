class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This is genuinely pissing me off because of how easy it is
        # sets have O(1) look up, (num-1) in numSet is fast
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest