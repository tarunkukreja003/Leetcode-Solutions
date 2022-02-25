class Solution:
    def romanToInt(self, s: str) -> int:
        """
        
        XIV -> X + IV -> 14
        
        XIX -> 19
        
        "IXCM" -> not a valid roman numeral
        
        
        travsere the string one by one
        
        if the current is I then check whether the next is V or X, if it is then include them and add the value do i+=2 in string traversal
        
        similarly for the rest of the 2 subtraction conditions
        
        
        
        """
        
        romanToIntegerMapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        i = 0
        integerValue = 0
        
        while i < len(s):
            print(i)
            if s[i] == "I":
                if i+1 < len(s) and s[i+1] == "V":
                    integerValue += 4
                    i += 2
                    
                elif i+1 < len(s) and s[i+1] == "X":
                    integerValue += 9
                    i += 2
                else:
                    integerValue += romanToIntegerMapping[s[i]]
                    i += 1
                    
                
            elif s[i] == "X":
                if i+1 < len(s) and s[i+1] == "L":
                    integerValue += 40
                    i += 2
                    
                elif i+1 < len(s) and s[i+1] == "C":
                    integerValue += 90
                    i += 2
                else:
                    integerValue += romanToIntegerMapping[s[i]]
                    i += 1
                    
            elif s[i] == "C":
                if i+1 < len(s) and s[i+1] == "D":
                    integerValue += 400
                    i += 2
                    
                elif i+1 < len(s) and s[i+1] == "M":
                    integerValue += 900
                    i += 2
                
                else:
                    integerValue += romanToIntegerMapping[s[i]]
                    i += 1
                    
            
            else:
                integerValue += romanToIntegerMapping[s[i]]
                i += 1
        
        return integerValue
            
        