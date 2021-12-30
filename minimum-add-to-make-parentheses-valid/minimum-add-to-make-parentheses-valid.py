class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # questions
        # the string can only have either ( or ) - yes
        
        # we'll use 1 stack to store opening brackets. When we encounter a ')' we'll check if stack is empty or not. If it is not just pop from the stack, if it is we'll increment a variable called countOpeningBracketsRequired. At the end we'll add countOpeningBracketsRequired and size of stack
        
        countOpeningBracketsRequired = 0
        openingBracketsStack = []
        
        for char in s:
            if char == '(':
                openingBracketsStack.append('(')
            elif char == ')':
                if openingBracketsStack:
                    openingBracketsStack.pop()
                else:
                    countOpeningBracketsRequired += 1
        
        stackSizeRemaining = 0
        if openingBracketsStack:
            stackSizeRemaining = len(openingBracketsStack)
        minimumParanthesisRequired = countOpeningBracketsRequired + stackSizeRemaining
        
        return minimumParanthesisRequired
        
        
        
        
        