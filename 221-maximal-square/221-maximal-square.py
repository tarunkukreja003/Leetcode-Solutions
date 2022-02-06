class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        we have to find the square with all 1's having largest area -> area = length^2
        
        m and n are minimum 1 ? yes
        
        is 0's and 1's in the form od string or number? - string 
        
        areas possible -> 1x1, 2x2, 3x3
        if I encounter a 1 it might be possible that its part of a bigger square or not
        
        
        maxArea = 0
        
        if the current is 1 and its bottom, right, down and right down diagnol neighbor is 1 then put it in the area -> increase length by 1 and do dfs, if anyone encounters 0 then just return 0 and thats the square and if its area is greater than maxArea then that's the max area 
        
        but the above is very naive solution since we'll do this for every 1 which has bottom, right, down and right down diagnol neighbor 1 , multiple 1's are being taken considered multiple times
        
        time complexity of this solution :
        
        n x m -> n rows and m columns
        
        (m x n)^2 
        
        
        ----------------
        
        Optimization
        
        we'll have to store the previous results and build on that
        
        
        1 1 0 0 0
        1 1 1 1 0
        0 1 1 1
        0 1 1 1
          
        
        dp
        
        1 1 0 0
        1 2 1 1
        0 1 2 2
        0 1 2 3
          
        if current is 1 and dp left, top, and top left diagnol are >0:
            if all left, top and top left are equal then:
                dp[i][j] = max(dp[i-1][j], dp[j-1][i], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[j-1][i], dp[i-1][j-1])
            
        else:
            dp[i][j] = givenMatrix[i][j]
        
        
        time complexity -> O(n x m)
        """
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[ 0 for j in range(m+1)] for i in range(n+1)]
        
        maxSqLen = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                # 
                if matrix[i-1][j-1] == '1':
                    # we are using min because let's say left  = 3(this element is a part of 3X3 square) , top left = 3 and top = 0 that means for the current element(rightmost and lowest element in the square -> last element in the square) the max length square that can be formed = 0 + 1 -> +1 because i-1 j-1 = 1 
                    # check solution for more clarity 
                    dp[i][j] = min(int(dp[i-1][j]), int(dp[i][j-1]), int(dp[i-1][j-1])) + 1
                    maxSqLen = max(maxSqLen, dp[i][j])

        
        print(dp)
        
        return maxSqLen**2
    
    """
    1 1 1 1 0
    1 1 1 1 0
    1 1 1 1 1
    1 1 1 1 1
    0 0 1 1 1 
    """
                    
        
        
        