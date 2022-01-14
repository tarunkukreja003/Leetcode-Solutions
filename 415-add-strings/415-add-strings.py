class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # "999" "98"
        
        """
        9 + 9 = 18
        
        carry will be either 0 or 1
        
        
        time complexity = O(max(len(num1), len(num2)))
        space complexity = O(max(len(num1), len(num2)))
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
                i -= 1
                j -= 1
            else:
                carry = 0
                sumOfNumsStr += str(sumOfNums)
                i -= 1
                j -= 1
        
        # if there are any left elements
        
        while i>=0:
            sumOfNums = int(num1[i]) + carry
            if sumOfNums > 9:
                carry = 1
                unitsDigit = sumOfNums % 10
                sumOfNumsStr += str(unitsDigit)
                i -= 1
            else:
                carry = 0
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
        
        # reverse the string to get the answer
        
        # reverse it without using storing the result in any other string
        
        # we'll use two pointers, one will start from begin and other from end and keep swapping until both pointers meet
        
        sumOfNumsStr = [sumOfNumsStr[i] for i in range(len(sumOfNumsStr))]
        # print(sumOfNumsStr)
        
        i = 0
        j = len(sumOfNumsStr)-1
        
        while i<=j:
            sumOfNumsStr[i], sumOfNumsStr[j] = sumOfNumsStr[j], sumOfNumsStr[i]
            i += 1
            j -= 1
            
        # print()
#         while k>=0:
#             finalSumStr += sumOfNumsStr[k]
#             k -= 1
        
        return "".join(sumOfNumsStr)
            
            
            
            
            
        