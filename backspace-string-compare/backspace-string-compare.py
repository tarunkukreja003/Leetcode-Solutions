class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        
        for char in s:
            if char != "#":
                stack1.append(char)
            else:
                if stack1:
                    stack1.pop()
        
        for char in t:
            if char != "#":
                stack2.append(char)
            else:
                if stack2:
                    stack2.pop()
        
        # minLen = min(len(stack1), len(stack2))
        
        if len(stack1) != len(stack2):
            return False
        
        for i in range(len(stack1)):
            if stack1[i] != stack2[i]:
                return False
            
        return True