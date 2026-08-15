class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for rows - is it possible?
        bot = 0
        top = len(matrix) - 1

        row = -1
        found = False
        while bot <= top and not found:
            mid = (top + bot) // 2
            # mid is the row we want if...
            # target in range matrix[mid][0] and matrix[mid][len(matrix[mid])-1]
            row_len = len(matrix[mid])
            if matrix[mid][0] > target:
                top = mid-1
            elif matrix[mid][row_len - 1] < target:
                bot = mid+1
            else:
                row = mid
                found = True
        
        if not found:
            return False
        
        # binary search for column
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        


