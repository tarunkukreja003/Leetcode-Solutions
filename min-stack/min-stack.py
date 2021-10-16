class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        # [], []
        self.originalStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:        
        # O(nlogn)
        self.originalStack.append(val)
        self.minStack = sorted(self.originalStack, reverse=True)
            
        
        

    def pop(self) -> None:
        # O(n)
        # if isEmpty():
        #     return -1
        self.originalStack.pop()
        self.minStack = sorted(self.originalStack, reverse=True)
        
        
        
        

    def top(self) -> int:
        return self.originalStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()