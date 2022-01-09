class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # questions
        # the string can only have either ( or ) - yes
        
        # we'll use 1 stack to store opening brackets. When we encounter a ')' we'll check if stack is empty or not. If it is not just pop from the stack, if it is we'll increment a variable called countOpeningBracketsRequired. At the end we'll add countOpeningBracketsRequired and size of stack
        
        countOpeningBracketsRequired = 0
        openingBracketsNumber = 0
        
        for char in s:
            if char == '(':
                openingBracketsNumber += 1
            elif char == ')':
                if openingBracketsNumber > 0:
                    openingBracketsNumber -= 1
                else:
                    countOpeningBracketsRequired += 1
        
        minimumParanthesisRequired = countOpeningBracketsRequired + openingBracketsNumber
        
        return minimumParanthesisRequired
        
        
        
        
        