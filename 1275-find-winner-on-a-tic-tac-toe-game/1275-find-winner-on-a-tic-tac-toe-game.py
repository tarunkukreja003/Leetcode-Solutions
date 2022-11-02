class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        
        what is pending?
        
        if we are on moves[8] and we check there is a winner or not, if not then return Draw
        
        check if alternate indices are in row, col or diaonal elements
        
        for A check 0, 2, 4 .. indices check if any 3 indices are in a row/col or diagnol
        for B check 1, 3, 5 .. indices check if any 3 indices are in a row/col or diagnol
        
        approach:
        for eveery element check if there are any other 2 indices in the same row/col or diagnol
        
        diagnol 1 => [0,0] [1,1] [2,2] => row == col
        diagnol 2 => [0,2] [1,1] [2,0] => sum of row and col == 2
        
        [0,0] [0,1] [1,0] -> not
        [0,0] [0,1] [0,2] -> yes
        
        [0,0] [0,1] [1,0] [2,0] -> yes
        
        
        [0,0] [1,1] [0,2] [2,0] -> yes
        
        """
        
        for index, coordinate in enumerate(moves):
            row = coordinate[0]
            col = coordinate[1]
            sumOfCoordinates = row + col
            countDiagnol1 = 0
            countDiagnol2 = 0
            rowSame = 0
            colSame = 0
            diagnol1PossibleFlag = False
            if row == col:
                diagnol1PossibleFlag = True
            print("checking for coordinate: ", coordinate)
            
            for j in range(index+2, len(moves), 2):
                # find the 2 indices which have either same row or col or have row = 
                
                
                # [1,1] is included in both diagnols
                rowNested, colNested = moves[j]
                if rowNested == colNested and diagnol1PossibleFlag:
                    countDiagnol1 += 1
                
                elif (rowNested + colNested) == sumOfCoordinates:
                    
                    countDiagnol2 += 1
                
                # either all 3 will have same row or same col, not 1 has same row and other has same col
                elif rowNested == row:
                    rowSame += 1
                elif colNested == col:
                    colSame += 1
                
                print("j: ", j)
                print("moves[j]: ", moves[j])
                print("count: ", count)
                print("rowSame: ", rowSame)
                print("colSame: ", colSame)
                print("index: ", index)
                
                
                if (countDiagnol1 == 2 and index%2==0) or (countDiagnol2 == 2 and index%2==0) or (rowSame == 2 and index%2==0) or (colSame == 2 and index%2==0):
                        return "A"
                elif (countDiagnol1 == 2 and index%2!=0) or (countDiagnol2 == 2 and index%2!=0)  or (rowSame == 2 and index%2!=0) or (colSame == 2 and index%2!=0):
                        return "B"
        if len(moves) != 9:
            return "Pending"
        return "Draw"
                
                
                
                
        
        