class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 4 variables
        topRow, bottomRow, leftCol, rightCol = 0, len(matrix)-1, 0, len(matrix[0])-1
        # print(rightCol)
        
        spiral1D = []
        while len(spiral1D) < len(matrix) * len(matrix[0]) :
            
            for i in range(leftCol, rightCol+1):
                print('topRow:   ', topRow)
                print('colNumber:   ', i)
                spiral1D.append(matrix[topRow][i])
            
            topRow += 1
            
            for j in range(topRow, bottomRow + 1):
                print('rightCol:  ', rightCol)
                print('rowNum:  ', j)
                spiral1D.append(matrix[j][rightCol])
            
            
            
            print('topRow just above !=:   ',  topRow)
            print('bottomRow just above !=:   ',  bottomRow)
            
            if topRow <= bottomRow:
                
                rightCol -= 1
            
                for i in range(rightCol, leftCol-1, -1):
                    print('bottomRow:   ', bottomRow),
                    print('colNumber:   ', i)
                    spiral1D.append(matrix[bottomRow][i])
            
            
            
            if leftCol <= rightCol:
                
                bottomRow -= 1
            
                for j in range(bottomRow, topRow-1, -1):
                    print('leftCol:  ', leftCol)
                    print('rowNum:   ', j)
                    spiral1D.append(matrix[j][leftCol])
            
            leftCol += 1
        
        
        return spiral1D
            
        