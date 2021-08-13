class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/
            
        biggerLen = max(len(a), len(b))
        a = a.zfill(biggerLen)
        b = b.zfill(biggerLen)
        result = ""
        carry=0
        
        
        
        for i in range(biggerLen - 1, -1, -1): ## now start doing addition from left to right
            digits_addition = carry
            digits_addition += 1 if a[i] == "1" else 0
            digits_addition += 1 if b[i] == "1" else 0
            
            result = ("1" if digits_addition % 2 == 1 else "0") + result
            
            carry = 0 if digits_addition < 2 else 1
        
        if carry != 0:
            result = "1" + result
        
        return result.zfill(biggerLen)
            
            
            
        