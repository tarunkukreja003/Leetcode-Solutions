class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # "999" "98"
        
        """
        9 + 9 = 18
        
        carry will be either 0 or 1
        """
        
        carry = 0
        
        sumOfNumsStr = ''
        i = len(num1) - 1
        j = len(num2) - 1
        
        while i>=0 and j>=0:
            # print(i,j)
            sumOfNums = int(num1[i]) + int(num2[j]) + carry
            # 17
            if sumOfNums > 9:
                carry = 1
                unitsDigit = sumOfNums % 10
                sumOfNumsStr += str(unitsDigit)
                # sumOfNumsStr += str(sumOfNums)
                i -= 1
                j -= 1
            else:
                carry = 0
                # print(sumOfNums)
                sumOfNumsStr += str(sumOfNums)
                i -= 1
                j -= 1
        
        # if there are any left elements
        
        while i>=0:
            sumOfNums = int(num1[i]) + carry
            if sumOfNums > 9:
                carry = 1
                unitsDigit = sumOfNums % 10
                # print(sumOfNumsStr)
                sumOfNumsStr += str(unitsDigit)
                i -= 1
            else:
                carry = 0
                # print(sumOfNums)
                sumOfNumsStr += str(sumOfNums)
                i -= 1
        
        while j>=0:
            sumOfNums = int(num2[j]) + carry
            if sumOfNums > 9:
                carry = 1
                unitsDigit = sumOfNums % 10
                sumOfNumsStr += str(unitsDigit)
                j -= 1
            else:
                carry = 0
                sumOfNumsStr += str(sumOfNums)
                j -= 1
        
        if carry == 1:
            sumOfNumsStr += str(carry)
            
        
        # print(sumOfNumsStr)
        
        finalSumStr = ''
        
        k = len(sumOfNumsStr)-1
        
        while k>=0:
            finalSumStr += sumOfNumsStr[k]
            k -= 1
        
        return finalSumStr
            
            
            
            
            
        