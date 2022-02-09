class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        """
        
        the suffix will become prefix and prefix will become suffix
        
        the prefix of s should be suffix of goal and suffix of s should be prefix of goal
        
        moreover, prefix + suffix should be equal to the length of the string
        both goal and s should have equal length
        
        prefix + suffix should not be intersecting
        
        we'll start with prefix of s check if it is equal to 
        
        if s and goal are the same strings return True
        
        
        time complexity -> 
        if you visit a character only once then only it is O(n)
        
        to check the rest of the string it is linear
        
        1 + 2 + 3 -> O(n^2)
        
        
        for KMP we'll have to find the longest proper prefix in s which is also a suffix in goal
        
        s + goal -> KMP on this
        
        
        KMP time complexity -> O(2N) n is the length of s or goal
        
        space complexity -> O(2N)
        
        """
        
        if len(s) != len(goal):
            return False
        
        def isEqualString(text1, text2):
            for i in range(len(text1)):
                if text1[i] != text2[i]:
                    return False
            return True
            
#         prefixS = ""
        
#         for i in range(len(s)):
#             prefixS = s[:i+1]
#             lenPrefix = i+1
#             if prefixS == goal[-lenPrefix:]:
#                 booleanVal = isEqualString(s[lenPrefix:], goal[:-lenPrefix])
#                 if booleanVal:
#                     return True
#                 else:
#                     return False
#         return False
            
                
        stringForKMP = s + goal
        
        lps = [0 for _ in range(len(stringForKMP))]
        lps[0] = 0
        
        j = 0
        i = 1
        
        while i < len(stringForKMP):
            if stringForKMP[i] == stringForKMP[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                
                if j > 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        
        
        if lps[-1] == 0:
            return False
        
        lenProperPrefixSuffix = lps[-1]
        
        booleanVal = isEqualString(s[lenProperPrefixSuffix:], goal[:-lenProperPrefixSuffix])
        if booleanVal:
            return True
        else:
            return False
        