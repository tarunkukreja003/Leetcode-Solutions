class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        """
        . -> matches any single character
        * -> zero or more occurences of the preceding element
        
        .*
        
        pattern should cover the entire string
        
        if pattern == ".*" then true -> this can match any string
        
        *. ->  not passible because * will always come after a valid character
        
        "abcfdfgi"
".*fgi"
        "aaa"
        "a."
        
        ".*"
        
        2 stars cannot be together
        
        basically we don't know the pattern
        
        * could be of any length of the previous element we don't know how much length do we need it for
        
        the first question is either to use * or not -> zero or more occurences of the previous element
        
        to answer whether to use * or not check current element in string with previous element of *, if they are same then we have to use * else don't use. If we don't use * then just move pattern pointer + 1
        
        if previous of * = current char of string then we need 1 or more occurence of previous element -> now we don't know how many
        
        
        
        
        first start will two pointers -> one on start of string and other on start of p
        
        match -> increment
        
        the problem is when we encounter * or .
        
        if pattern contains .* then the string ahead is matched
        
        
        
        "abcdrf"
        ".*cgt"
        
        https://levelup.gitconnected.com/solving-for-recursive-complexity-736439987cb0
        
        text[i:] -> i will be from 0 to T
        pattern[2j:] -> j will be from 0 to P/2
        
        
        first understand recursion leetcode solution
        then the following video DP solution
        
        DP approach - similar to recursion, just bottom-up
        https://www.youtube.com/watch?v=l3hda49XcDE
        
        
        
        dp[i][j] =  {
        
        
        
                                                    
        
        }
        
        
        """
        
        lenText = len(text)
        lenPattern = len(pattern)
        dp = [[False for _ in range(lenPattern + 1)] for _ in range(lenText + 1)]
        
        # if both pattern and text are empty
        dp[0][0] = True
        
        # if pattern = "a*", "a*b*" text = ""
        
        for j in range(1, lenPattern+1):
            if pattern[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, lenText+1):
            for j in range(1, lenPattern+1):
                
                if text[i-1] == pattern[j-1] or pattern[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1] == "*":
                    dp[i][j] = dp[i][j-2] 
                    # one or more occurence
                    if text[i-1] == pattern[j-2] or pattern[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j] 
                        
        return dp[lenText][lenPattern]
        
        
        
        
        