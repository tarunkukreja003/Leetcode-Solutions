class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """
        
        if we replace then at that time the string is not updated
        
        run the loop till k
        i in range k
        
        start matching sources[i] string with s[i:]
        if any character is not equal
        then just the current string cannot be replaced
        and continue with the next i
        
        if all match then store it in array of output strings
        
        indices are not sorted
        []
        
        how will we find the remaining string which is not replaced
        
        "-b--"
        {
        0: "eee"
        2: "ffff"
        }
        
        "eeebffff"
        
        "vbfrssozp"
        """
        
        def matchStringSameLen(str1, str2):
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return False
            return True
        
            
        i = 0
        
        startIndexToReplaceStringMap = {}
        outputString = ""
        inputStringIntoList = list(s)
        
        k = len(indices)
        while i < k:
            substringLen = len(sources[i])
            startIndex = indices[i]
            
            isMatch = matchStringSameLen(s[startIndex:startIndex + substringLen], sources[i])
            
            if isMatch:
                startIndexToReplaceStringMap[startIndex] = (targets[i], substringLen)
                                                            
                # replace substring in original string by placeholder value
                # print(startIndex)
                # print(substringLen)
                for j in range(startIndex, startIndex + substringLen):
                    inputStringIntoList[j] = "-"
            
            i += 1
                    
        # print(inputStringIntoList)   
        # print(startIndexToReplaceStringMap)
        
        index = 0
        while index < len(inputStringIntoList):
            # print(index)
            if inputStringIntoList[index] != '-':
                outputString += inputStringIntoList[index]
                index += 1
            else:
                # if s[index] == '-' -> copy the contents from hashmap with the same start index and do index += until all - are over
                
                outputString += startIndexToReplaceStringMap[index][0]
                # we need to skip '-' until length of the original word
                subStrLen = startIndexToReplaceStringMap[index][1]
                # print("subStrLen: ", subStrLen)
                index += subStrLen
        
        return outputString
                        
                
                

                
            
            