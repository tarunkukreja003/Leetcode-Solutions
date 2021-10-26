class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        
        # enqueue the new element to q2
        self.q2.append(x)
        
        # deque all the elements from q1 and enqueue to q2
        while self.q1:
            currentElement = self.q1[0]
            self.q2.append(currentElement)
            self.q1 = self.q1[1:]
        
        # swap q1 and q2, the idea is that q2 should always be empty when a new element is being pushed
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        poppedElement = self.q1[0]
        self.q1 = self.q1[1:]
        return poppedElement
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        
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

