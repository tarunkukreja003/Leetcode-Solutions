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
        
        
        @lru_cache(maxsize=None)
        def findLCS(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                # move both the pointers
                return findLCS(i+1, j+1) + 1 
            
            else:
                # move either pointer
                return max(findLCS(i+1, j), findLCS(i, j+1))        
        
        return findLCS(0,0)