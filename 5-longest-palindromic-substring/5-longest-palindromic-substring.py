class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        palindrome -> should be the same when read forward and backward
        
        let's maintain 2 pointers one at the start other at the end
        
        base case
        if odd
        P(i,i) = True
        
        if even 
        P(i,i+1) => s[i] == s[i+1]
        
        
        
        P(i,j) => boolean -> true if palindrome(i+1, j-1) and s[i] == s[j]
        P(i, j) = P(i+1, j-1) and s[i] == s[j]
        
        https://leetcode.com/problems/longest-palindromic-substring/discuss/555413/Python-Approach-3
        
        https://www.youtube.com/watch?v=XYQecbcd6_c - there are 2 centers on even length and 1 in odd length 
        
        "cdbbdccc"
         
            
            
        """
        
        # We'll be doing expand around center approach as in the above video
        
        # if there is just 1 character then that's the answer
        
        # if there are 2 characters then there are 2 centers and we can expand around both of them
        
        # we'll expand around every character
        
        def expandAroundCenter(left, right):
            
            currPalindrome = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currPalindrome = s[left:right+1]
                left -= 1
                right += 1
            
            return currPalindrome
                
                
        longestPalindromeSubstring = ""
        for i in range(len(s)):
            
            
            # odd length
            oddCenterExpandSubstring = expandAroundCenter(i, i)
            
            # even length
            evenCenterExpandSubstring = expandAroundCenter(i,i+1) # it could have been i-1 if we would have started i = 1
            
            maxSubstring = ""
            if len(oddCenterExpandSubstring) > len(evenCenterExpandSubstring):
                maxSubstring = oddCenterExpandSubstring
            else:
                maxSubstring = evenCenterExpandSubstring
            
            if len(maxSubstring) > len(longestPalindromeSubstring):
                longestPalindromeSubstring = maxSubstring
        
        return longestPalindromeSubstring
                
                
        
        
        
        
            
        