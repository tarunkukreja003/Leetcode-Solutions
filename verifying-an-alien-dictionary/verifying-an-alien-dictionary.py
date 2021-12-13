class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # make a dictionary like {"w": 0, "h":1}
        
        # is the order string contain unique characters? - yes
        # is the length of order only 26 or large value? - large variable value
        # what if the words are same till the length of the minimum length of the two? - then they'll be in order
        
        alienOrderDictionary = {}
        
        for i in range(len(order)):
            if order[i] not in alienOrderDictionary:
                alienOrderDictionary[order[i]] =  i
        
        print(alienOrderDictionary)
        
        # think of how two words will return False
         
        for j in range(len(words)-1):
            currStrLen = len(words[j])
            nextStrLen = len(words[j+1])
            minLength = min(currStrLen, nextStrLen)
            
            count = 0
            for k in range(minLength):
                if alienOrderDictionary[words[j][k]] > alienOrderDictionary[words[j+1][k]]:
                    return False
                if alienOrderDictionary[words[j][k]] < alienOrderDictionary[words[j+1][k]]:
                    break
                else:
                    count += 1
        
            # ["apple", "app"] - False
            # if both are equal and the length of the jth string > j+1th string then False
            if count == minLength and (currStrLen > nextStrLen):
                return False
        
        return True
        
        
        