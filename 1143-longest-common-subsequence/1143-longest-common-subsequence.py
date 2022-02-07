class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        """
        
        text1[:j]
        text2[:i]
        determine the longest common subsequence for the above strings => lcs[i][j]
        
        text1 = "abtfcde", text2 = "agce"
                      i                j   -> at this stage I don't know which pointer to move forward because if I move i, it will keep on moving till the end, if I move j it will keep on moving till the end, so we can move either 
                 
        longest common subsequence len = 
        
        stack = [1,1,1]
        
        
        so we can either move i or j
        
        
        findLCS(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                # move both the pointers
                return findLCS(i+1, j+1) + 1 
            
            else:
                # move either pointer
                return max(findLCS(i+1, j), findLCS(i, j+1))
                
            
        
        
        """
        
        # bottom-up 
        
        # initialise dp array, here there are 2 states, hence 2d array. Since we are finding the max length of common subsequence, length cannot be negative hence we set default values to 0
        
        lenText1 = len(text1)
        lenText2 = len(text2)
        dp = [[0 for _ in range(lenText2+1)] for _ in range(lenText1+1)]
        
        # set the base case and return value
        
        # default val -> if we reach lenText2 or lenText1 then its 0
        
        for i in range(lenText1):
            dp[i][lenText2] = 0
        
        for j in range(lenText2):
            dp[lenText1][j] = 0
        
        # we'll use nested for loops 
        
        # we'll be traversing backwards
        
        for i in range(lenText1-1,-1,-1):
            for j in range(lenText2-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
        return dp[0][0]
        