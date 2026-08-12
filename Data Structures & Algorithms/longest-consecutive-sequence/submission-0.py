class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        longest = 0

        for num in nums:
            # Ignore duplicates
            if num in lengths:
                continue

            left_length = lengths.get(num - 1, 0)
            right_length = lengths.get(num + 1, 0)

            new_length = left_length + 1 + right_length

            # Mark num as processed
            lengths[num] = new_length

            # Update the boundaries of the merged interval
            left_boundary = num - left_length
            right_boundary = num + right_length

            lengths[left_boundary] = new_length
            lengths[right_boundary] = new_length

            longest = max(longest, new_length)

        return longest