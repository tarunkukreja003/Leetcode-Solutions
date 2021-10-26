class Solution:
    def firstUniqChar(self, s: str) -> int:
        characterDict = {}
        
        # {
        #   l: [frequencyCounter, [list of index]]
        # }
        
        for i, char in enumerate(s): # O(n)
            if char not in characterDict:
                characterDict[char] = [1, [i]]
            else:
                characterDict[char][0] += 1
                characterDict[char][1].append(i)
        
        minIndex = float('inf')
        nonRepeatChar = ''
        flag = False
        for char, valList in characterDict.items():
            if valList[0] == 1:
                flag = True
                if minIndex > valList[1][0]:
                    minIndex = valList[1][0]
                    nonRepeatChar = char
        
        if flag == False:
            return -1
        
        return minIndex
            
        