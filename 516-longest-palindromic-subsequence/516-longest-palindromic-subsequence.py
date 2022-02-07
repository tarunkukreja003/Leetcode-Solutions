class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        
        "baab"
         
        
        "thybbbbburg"
            i   j
        
        length = 5
        "cbbd"
          ij
        
        
        ----------------
    
    
    
    def longestPalindromeSubseq(i, j):
    
        if i > j:
            return 0
        if i == j:
            return 1
        
        if s[i] == s[j]:
         return 2 + longestPalindromeSubseq(i+1, j-1)
        
        elif s[i] != s[j]
            return max(longestPalindromeSubseq(i, j-1), longestPalindromeSubseq(i+1, j))
        
        
    
        
        """
        
#         @lru_cache(maxsize=1000)
#         def palindromeSubseq(i, j):
#             if i > j:
#                 return 0
#             if i == j:
#                 return 1

#             if s[i] == s[j]:
#              return 2 + palindromeSubseq(i+1, j-1)

#             elif s[i] != s[j]:
#                 return max(palindromeSubseq(i, j-1), palindromeSubseq(i+1, j))

        
#         return palindromeSubseq(0, len(s)-1)


    # bottom-up
    
    # https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
    
    # in this dp[i][j] means str[i:j+1]
    # and j-i+1 = lengthOfSubsequence
    # so j and i are related, if we know i we can find out j -> we don't need separate loops for i and j
    
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # lengthOfSubsequence = 1 has been calculated
        for i in range(n):
            dp[i][i] = 1
            
#             if i + 1 < n and s[i] == s[i+1]:
#                 dp[i][i+1] = 2
        
        # let's find subsequence of length >= 2
        for lengthOfSubsequence in range(2, n+1):
            # i will go from 0 to n-2 if the minimum length of subsequence is 2 because j will be at n-1
            for i in range(n-lengthOfSubsequence+1):
                j = lengthOfSubsequence + i - 1
                
                if s[i] == s[j] and lengthOfSubsequence == 2:
                    dp[i][j] = 2
                # if i = 0, j = 1, lengthOfSubsequence = 2 and if s[i] == s[j] then dp[0][1] = 2+dp[0+1][1-1] => dp[1][0]  
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        # print(dp)
        return dp[0][n-1]  # we have to find start with the whole string str[0:n-1+1] => str[0:n]  
    
    
    """
    n = 3
    
    3x3 matrix will all 0 values
    
    
    1 2 3
    0 1 2
    0 0 1
    """