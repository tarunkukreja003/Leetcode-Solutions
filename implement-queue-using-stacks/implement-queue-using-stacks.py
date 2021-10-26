class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        # will only push to stack1
        self.stack1.append(x)
        
        

    def pop(self) -> int:
        # here we'll pop elements from stack1 and push them to stack2 and pop element from
        # stack2 and again pop elements from stack2 and push them back to stack 1mpty
        if self.empty():
            return 
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1])
            self.stack1 = self.stack1[:-1]
        
        poppedElement = self.stack2[-1]
        
        self.stack2 = self.stack2[:-1]
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2 = self.stack2[:-1]
        
        return poppedElement
        
        
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# s1 = 
# s2 = 