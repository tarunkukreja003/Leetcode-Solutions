class MinStack(object):

    def __init__(self):
        self.minStack = []
        self.minElement = float('inf')
        self.minElementStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minStack.append(val)
        if self.minElement >= val:
            self.minElement = val
            self.minElementStack.append(self.minElement)
        
            
        

    def pop(self):
        """
        :rtype: None
        """
        
        if self.minStack:
            poppedElement = self.minStack.pop()
            if poppedElement == self.minElement:
                self.minElementStack.pop()
                if self.minElementStack:
                    self.minElement = self.minElementStack[-1]
                else:
                    self.minElement = float('inf')
    def top(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
get the min of stack in O(1) time



 it is not necessary that minimum element should be at the top of the stack, we just have to ge the minimum element


minStack = [0,1,0]
minElement = 0

minElementStack = [0]

if poppedElement == minElement:
    minElement = minElementStack.pop()


"""


