class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        direct KMP
        
        
        """
        
        if len(needle) == 0:
            return 0
        
        if len(haystack) == 0:
            return -1
        
        def computeLPSArray(pattern):
            lenPattern = pattern
            lps = [0 for _ in range(len(pattern))]
            lps[0] = 0
            j = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    
                    if j > 0:
                        j = lps[j-1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps
        
        def kmpSearch(haystack, needle):
            n = len(haystack)
            m = len(needle)
            
            lps = computeLPSArray(needle)
            
            j = 0
            i = 0
            
            while i < n:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                
                if j == m:
                    return (i - j)
                
                elif i < n and  haystack[i] != needle[j]:
                    
                    if j > 0:
                        j = lps[j-1]
                    else:
                        i += 1
            return -1
                        
        return kmpSearch(haystack, needle)
        
        