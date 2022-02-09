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
        
        """
        
        if len(s) != len(goal):
            return False
        
        def isEqualString(text1, text2):
            for i in range(len(text1)):
                if text1[i] != text2[i]:
                    return False
            return True
            
        prefixS = ""
        
        for i in range(len(s)):
            prefixS = s[:i+1]
            lenPrefix = i+1
            if prefixS == goal[-lenPrefix:]:
                booleanVal = isEqualString(s[lenPrefix:], goal[:-lenPrefix])
                if booleanVal:
                    return True
                else:
                    return False
        return False
            
                
        