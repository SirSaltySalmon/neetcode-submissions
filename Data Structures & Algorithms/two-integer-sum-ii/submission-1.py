class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end_i = len(numbers) - 1
        start_i = 0
        
        # Then look for combination
        two_sum = numbers[end_i] + numbers[start_i]
        while two_sum != target:
            if two_sum > target:
                end_i -= 1
            elif two_sum < target:
                start_i += 1
            two_sum = numbers[end_i] + numbers[start_i]
        
        return [start_i + 1, end_i + 1]