class Solution:
    def removeDuplicates(self, s: str) -> str:
        # brute-force approach -> to go over 
        
        # recursion -> we'll start the recursion from the first duplicate, let's say i and i+1 are duplicates, then in the next recursion step we'll pass str[:i-1] + str[i+2:] - this will be O(n^2)
        
        # think of storing the current character and then retreiving it
        
        # stack
        
        # on the current char check if top of element is same as str[i], if it is then pop from stack and move to the next character in the string, if it is not then push into the stack
        
        # at the end just empty the contents of the stack in a string a reverse the string
        
        i = 0
        
        characterStack = []
        while i < len(s):
            if characterStack and characterStack[-1] == s[i]:
                characterStack.pop()
                i += 1
            else:
                characterStack.append(s[i])
                i += 1
        
        finalStr = ''
        
        for char in characterStack:
            finalStr += char
        
        # print(characterStack)
        
        return finalStr
        
        
        