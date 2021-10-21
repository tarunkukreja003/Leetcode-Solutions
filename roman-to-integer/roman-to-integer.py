class Solution:
    def romanToInt(self, s: str) -> int:
        # traversing from back to front
        romanToIntegerdict = {
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000 
        }
        i = len(s) - 1
        
        integerSum = 0
        while i >= 0:
            if (s[i] == "V") or (s[i] == "X"):
                if (i-1>=0) and (s[i-1] == "I"):
                    integerSum += romanToIntegerdict[s[i]] - romanToIntegerdict[s[i-1]]
                    i -= 2
                else:
                    integerSum += romanToIntegerdict[s[i]]
                    i -= 1
            
            elif (s[i] == "L") or (s[i] == "C"):
                if (i-1>=0) and (s[i-1] == "X"):
                    integerSum += romanToIntegerdict[s[i]] - romanToIntegerdict[s[i-1]]
                    i -= 2
                else:
                    integerSum += romanToIntegerdict[s[i]]
                    i -= 1
            
            elif (s[i] == "D") or (s[i] == "M"):
                if (i-1>=0) and (s[i-1] == "C"):
                    integerSum += romanToIntegerdict[s[i]] - romanToIntegerdict[s[i-1]]
                    print(integerSum)
                    i -= 2
                else:
                    integerSum += romanToIntegerdict[s[i]]
                    print(integerSum)
                    i -= 1
            
            else:
                integerSum += romanToIntegerdict[s[i]]
                i -= 1
        
        return integerSum
                
            
            
        
        