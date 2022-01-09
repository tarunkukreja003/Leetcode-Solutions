class Solution:
    def maximumSwap(self, num: int) -> int:
        # first convert the number into a list of digits
        # maxNumber = currNumber
        # swap every digit with every other digit -> O(n^3)
        
        # first digit of the number should be the maximum digit, if it is already then the next digit should be second highest digit
        
        # sort the list of digits and compare it with the original digits list
        
        # [6,3,7,2], [2,3,6,7] {2:3, 7:2, 3:1, 6:0}
        
        # [6,3,2,7]
        
        originalDigitsList = []
        indicesOfDigitsDict = {}
        sortedDescDigitsList = []
        
        while num > 0:
            digit = num % 10
            originalDigitsList.append(digit)
            num = num // 10
        
        # print(originalDigitsList)
        
        index = 0
        
        while index < len(originalDigitsList):
            if originalDigitsList[index] not in indicesOfDigitsDict:
                indicesOfDigitsDict[originalDigitsList[index]] = index
            
            index += 1
        
        # print(indicesOfDigitsDict)
        
        sortedDescDigitsList = sorted(originalDigitsList)
        
        for i in range(len(sortedDescDigitsList)-1,-1,-1):
            if sortedDescDigitsList[i] != originalDigitsList[i]:
                # swap 
                index = indicesOfDigitsDict[sortedDescDigitsList[i]]
                originalDigitsList[i], originalDigitsList[index] = originalDigitsList[index], originalDigitsList[i]
                break
        
        # print(originalDigitsList)
        
        i = len(originalDigitsList) - 1
        
        maxNum = 0
        while i >= 0:
            maxNum = originalDigitsList[i] + 10*maxNum
            i -= 1
            
        
        return maxNum
        
        
                
                
                
        
        