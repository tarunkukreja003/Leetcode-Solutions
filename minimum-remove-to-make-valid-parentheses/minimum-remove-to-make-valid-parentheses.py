class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # an opening bracket should come before a closing bracket
        #
        # stack -> push the ( and if you encounter ) pop from stack, if there is nothing to pop from stack then put (')',0) in the list
        
        # put index of ( in stack like ('(', 1)
        # at the end of the string check if the stack is empty, if it is then that's the answer, if its not then don't take the ( at that index
        
        # while adding in the final string list, add every type of character, even )
        
        # skip the current iteration - this is the iteration in final string list
        
        bracketsStack = []
        finalisedStringList = []
        for i in range(len(s)):
            if s[i] == '(':
                bracketsStack.append(('(', i))
                finalisedStringList.append(('(', i))
            elif s[i] == ')':
                if bracketsStack:
                    bracketsStack.pop()
                    finalisedStringList.append(')')
                else:
                    finalisedStringList.append((')', 0))
            
            else:
                finalisedStringList.append(s[i])
                
        
        finalReverseString = ''
        for i in range(len(finalisedStringList)-1, -1, -1):
            if finalisedStringList[i] == (')', 0):
                continue
            elif finalisedStringList[i] == ('(', i):
                if bracketsStack and bracketsStack[-1] == ('(', i):
                    bracketsStack.pop()
                    continue
                else:
                    finalReverseString += '('
            else:
                finalReverseString += finalisedStringList[i]
                
        finalStr = ''
        
        for i in range(len(finalReverseString)-1, -1, -1):
            finalStr += finalReverseString[i]
            
        return finalStr
                
                    
                
                    
                
            
            
            
        
        
        
        
        
        