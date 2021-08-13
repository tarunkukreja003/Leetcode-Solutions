class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        digitsArray = []

        
        while x != 0:
            digit = x % 10
            x = x // 10
            digitsArray.append(digit)
        
        
        i, j = 0, len(digitsArray) - 1
        
        while i<=j:
            if digitsArray[i] == digitsArray[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
            
        