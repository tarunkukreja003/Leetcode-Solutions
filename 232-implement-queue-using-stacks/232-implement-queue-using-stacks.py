class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        
        O(1)
        """
        
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        O(n)
        """
        
        if not self.empty():
        
            while len(self.stack1) > 1:
                topElement = self.stack1.pop()
                self.stack2.append(topElement)

            poppedElement = self.stack1.pop()
            
            while len(self.stack2) != 0:
                topElementStack2 = self.stack2.pop()
                self.stack1.append(topElementStack2)
                
            return poppedElement
        
        else:
            return "Queue is empty"
        
        
        

    def peek(self):
        """
        :rtype: int
        O(1)
        """
        if len(self.stack1) > 0:
            return self.stack1[0] 
        

    def empty(self):
        """
        :rtype: bool
        O(1)
        """
        
        if len(self.stack1) > 0:
            return False
        return True
        

"""

stack1 = [2]
stack2 = []

we'll use stack1 for push in O(1) time
in pop operation, we'll empty the contents of stack1 into stack2 until len(stack1) > 1

as soon as len(stack1) == 1, it will break and we can pop out the last element in stack1 and then put back elements from stack2 to stack1

O(n) pop operation and O(1) push operation

queue = [2]

"""
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()