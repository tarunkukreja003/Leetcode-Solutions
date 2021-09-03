class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # first checking for distinct elements in rows
        for i in range(9):
            temp_digit_dict = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in temp_digit_dict:
                    temp_digit_dict[board[i][j]] = 1
                else:
                    return False
        
        # checking for distinct elements in columns
        
        for col in range(9):
            temp_col_dict = {}
            for row in range(9):
                print("inside col", row, col)
                if board[row][col] == '.':
                    continue
                if board[row][col] not in temp_col_dict:
                    temp_col_dict[board[row][col]] = 1
                else:
                    return False
        
        # checking for the sub-box 3 x 3
        for x in range(3):
            for y in range(3):
                temp_matrix_dict = {}
                for i in range(x*3, x*3 + 3):
                    for j in range(y*3, y*3 + 3):
                        print(i, j)
                        if board[i][j] == '.':
                            continue
                        if board[i][j] not in temp_matrix_dict:
                            temp_matrix_dict[board[i][j]] = 1
                        else:
                            return False
        
        return True
                        
        
            
        