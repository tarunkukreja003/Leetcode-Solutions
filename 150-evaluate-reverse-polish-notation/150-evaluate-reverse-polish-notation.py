class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        division between two integers should truncate toward zero - this means 
        that -1/2 should be 0, not -1
        
        reverse polish notation -> postfix notation
        
        if token length is 1 and that is an integer then return that integer
        
        we can maintain a stack of integers
        
        if the current is an integer then put it onto the stack
        if the current is an operator then pop from the stack and do current operation 
        
        10 - (-11)
        
        -11 - 10
        
        we need to decide which operand will come on left or right of the operator
        
        we can push into the stack the index along with the integer
        when we pop from the stack we compare the indices of the popped integer and the running operation, the one which has greater index will come to the right of the operator
        after the operation is performed index of running operation = max(index of running operation, index of popped integer)
        
        if runningOperation == None then pop 2 integers from the stack and assign it the index of the integer which was popped first
        
        if the operator is / we'll do int(/)
        
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        stack = []
        
        runningOperation = 9 + 3 = 12 * -11 = 6 / -132 = 10 * 0 = 0 + 17 = 17 + 5 = 22
        index of runningOperation = 11
        
        
        
        10*6 - 0
        
        6 - 10
        
        
        ["4","-2","/","2","-3","-","-"]
        stack = [-2,5]
        -2 - 5
        index = 1
        
        
        """
        
        stackOfIntegers = []
        result = None
        
        if len(tokens) == 1:
            return int(tokens[0])
        for i, token in enumerate(tokens):
            # if operand
            if (token[0] == "-" and token[1:].isdigit()) or (token.isdigit()):
                stackOfIntegers.append(int(token))
            # if operator
            else:
                integer1 = stackOfIntegers.pop() 
                integer2 = stackOfIntegers.pop() 
                
                if token == "/":
                    result = int(integer2 / integer1)
                    stackOfIntegers.append(result)
                elif token == "*":
                    result = integer2 * integer1
                    stackOfIntegers.append(result)
                elif token == "-":
                    result = integer2 - integer1
                    stackOfIntegers.append(result)
                elif token == "+":
                    result = integer2 + integer1
                    stackOfIntegers.append(result)  
        
        return result

                
            
        