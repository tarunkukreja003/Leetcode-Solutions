import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Queue
        charFrequencyDict = collections.Counter(s)
        
        flag = False
        for i, char in enumerate(s):
            if charFrequencyDict[char] == 1:
                flag = True
                return i
        
        if flag == False:
            return -1
        
        
        