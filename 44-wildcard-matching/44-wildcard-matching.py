class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        
        Questions step by step: 
        
        
        Case 1:
        
        "jfnfjr"
        "jhf"
        
        match the pattern with the given string -> pattern only contains lowercase characters and text also contains lowercase english characters 
        
        algorithm:
        
        Naive: sliding window keep matching every character with every other character of the text
        worst case: when the last character of the pattern doesn't match with the last character of the text or all the characters in the text and the pattern are the same
        O(mn)
        
        Optimal: KMP algorithm -> O(m+n)
        
        Case 2:
        
        if we introduce a ? character in the pattern. '?' means it can match any single character
        
        the algorithm will still be the same just keep on matching , in the match condition if pattern[j] == "?" or text[i] == pattern[j]
        
        complexity = O(2n) -> n being the length of both the pattern and text
        
        Case 3:
        
        the current question
        
        
        * -> match any sequence of characters including an empty sequence
        
        ""
        "*" -> Matched True
        
        "abc"
        "*" -> True
        
        can 2 star come together ? - yes
        
        "**"
        
        
        "abcder"
        "*?dtr"   -> False
        
        so there is a limit till where a * has to match
        
        "abc"
        "a***"  -> True
        
        
        
        "abc"
        "a***dt" -> False
        
        text
        pattern
        
        
        matchString(pattern, text):
            if not pattern:
                return not text   # id text has also reached its end then this will return True, if text has not reached end then this will return False
            
            if bool(text) and text[0] == pattern[0] or pattern[0] == '?':
                # its a match
                matchString(pattern[1:], text[1:])
                

            elif pattern[0] == '*':
                either we'll consider the * or we will not
                if we consider *
                    recursiveCall(pattern, text[1:])

                if we don't consider *:
                    recursiveCall(pattern[1:], text)


            
        
        ----------------
        Time complexity -> 
        
        everytime we encounter a * there is 2 recursion calls
        
        "ofjoirigfriuhgiurfjdnfr"
        *
        
        O(t+p . 2^(t+p))
        
        
        we are recomputing the sub-problems which are already computed
        
        let's say I want to check whether pattern[2:] matches with text[1:]
        
        
        we can store the results of the sub-problems already computed
        
        
        
        
        
        """
        
        patternLength = len(p)
        textLength = len(s)
        
        matchedStringMatrix = [[False for _ in range(patternLength+1)] for _ in range(textLength+1)]
        
        matchedStringMatrix[0][0] = True
        
        #""
        #"**********"
        
        for j in range(1,patternLength+1):
            if p[j-1] == "*":
                matchedStringMatrix[0][j] = matchedStringMatrix[0][j-1]
        
        
        for i in range(1, textLength + 1):
            for j in range(1,patternLength+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    matchedStringMatrix[i][j] = matchedStringMatrix[i-1][j-1]
                elif p[j-1] == "*":
                    matchedStringMatrix[i][j] = matchedStringMatrix[i-1][j] or matchedStringMatrix[i][j-1]
                
        
        
        return matchedStringMatrix[textLength][patternLength]
            
        
        