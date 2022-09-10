class MyStack(object):
    from collections import deque

    def __init__(self):
        self.q1=deque([])
        self.q2 = deque([])
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        ## empty the contents of reverse q1 into q2 then popleft from q2 and then again reverse traverse q2 and empty into q1
        
        while not self.empty():
            lastElement = self.q1.pop()
            self.q2.append(lastElement)
        
        topOfStack = self.q2.popleft()
        
        while self.q2:
            lastElement = self.q2.pop()
            self.q1.append(lastElement)
        
        return topOfStack
        
        

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.q1[-1]
        else:
            return "List is empty"
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


"""
stack = [9, 10]

q1 = deque([9, 10])
q2 = deque([10,9])

pop will be O(n)
push will be O(1)

"""