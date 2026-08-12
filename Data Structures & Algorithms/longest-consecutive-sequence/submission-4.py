class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        longest = 0

        nums = set(nums)

        for num in nums:
            # Ignore duplicates
            if num in lengths:
                continue

            # If the boundaries don't exist
            # Then it cannot be continued using them, 0 length worth
            left_length = lengths.get(num - 1, 0)
            right_length = lengths.get(num + 1, 0)

            # But the num itself will be added anyway, 1 length worth
            new_length = left_length + 1 + right_length

            # Mark num as processed
            lengths[num] = new_length

            # Update the boundaries of the merged interval
            left_boundary = num - left_length
            right_boundary = num + right_length

            lengths[left_boundary] = new_length
            lengths[right_boundary] = new_length

            longest = max(longest, new_length)

        # This approach is really cool because it only needs to update
        # at the boundary. Example: 2, 3, 4, and 5 is getting added?
        # 2 length updates, 5 length updates, but 3 and 4 can chill cause
        # they are not ever considered anymore when adding a new piece in

        # Main idea is, it is efficient because only boundaries are considered
        return longest