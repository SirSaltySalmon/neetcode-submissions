from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_present = defaultdict(list)
        col_present = defaultdict(list)

        for i in range(3):
            for j in range(3):
                #These two loops are to check each of the 9 sub-boxes
                # 0 to 9, right to left, top to down
                current_box = []
                for k in range(3):
                    for l in range(3):
                        #And these two are for individual indexes
                        row_index = i * 3 + k
                        col_index = j * 3 + l
                        
                        number = board[row_index][col_index]

                        if number != ".":
                            if number in row_present[row_index]:
                                return False
                            else:
                                row_present[row_index].append(number)
                            
                            if number in col_present[col_index]:
                                return False
                            else:
                                col_present[col_index].append(number)
                        
                            if number in current_box:
                                return False
                            else:
                                current_box.append(number)
        
        return True
