class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        
        baba
        
        bbbb
        
        
        take prefix starting from len = 1 and then match in the string, if it matches then match with string[i+len]
        
        I'll only the whole string once we have found the pattern
        
        "abcabc" -> O()
            abc
            
            1 + 2 + 3 ... + n-1 = O(n^2)
         https://leetcode.com/problems/repeated-substring-pattern/discuss/487699/or-Java-or-Solution-in-or-O(n)-or-using-or-KMP-or - great solution
         
         time complexity -> 
        """
        
        pattern = ""
        lenPattern = 0
        
        matchedTillIndex = 0
        for i in range(len(s)-1):
            pattern = s[:i+1]
            lenPattern = i+1
            matchedTillIndex = i+1
            for j in range(i+1, len(s), lenPattern):
                if lenPattern+j > len(s):
                    break
                if lenPattern < len(s) and pattern != s[j:lenPattern+j]:
                    break
                matchedTillIndex += lenPattern
            
            if matchedTillIndex == len(s):
                return True
        
        return False
            
        
        