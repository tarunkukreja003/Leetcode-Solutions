class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        if len(S) == 0:
            return True
        for char in S:
            if (char == '(') or (char == '[') or (char == '{'):
                stack.append(char)
            if (char == ')'):
                if (len(stack) != 0) and (stack[-1] == '('):
                    stack.pop()
                else:
                    return False

            if (char == ']'):
                if (len(stack) != 0) and (stack[-1] == '['):
                    stack.pop()
                else:
                    return False

            if (char == '}'):
                if (len(stack) != 0) and (stack[-1] == '{'):
                    stack.pop()
                else:
                    return False


        if len(stack) != 0:
            return False

        return True
        