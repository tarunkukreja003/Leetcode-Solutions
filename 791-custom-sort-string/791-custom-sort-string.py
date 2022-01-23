class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        if there is no common character then return s
        
        order = "rk", s = "kriklri" 
        
        s: {
        k:2,
        r:2,
        i:2
        l:1
        } -> hashmap of s
        
        
        permuteStr = 'rrkkiil'
        
        
        create a hashmap of s, its keys will be alphabets and value will be frequency of alphabet
        create an empty str permuteStr
        then traverse order, if a char in order is in hashmap then append that alphabet to permuteStr frequency number of times and then set its frequncy to 0
        
        once we have traversed the order, we'll go through the hashmap of s. If s contains any alphabet whose frequncy >0 then append that alphabet to permuteStr frequency number of times
        
        time complexity -> len(order)-> m len(s) -> n O(n + m)
        space complexity -> O(m)
        
        
        """  
        
        sHashMap = {}
        permuteStr = ''
        
        for char in s:
            if char not in sHashMap:
                sHashMap[char] = 1
            else:
                sHashMap[char] += 1
                
        
        for char in order:
            if char in sHashMap:
                frequencyOfAlphabet = sHashMap[char]
                permuteStr += char*frequencyOfAlphabet
                sHashMap[char] = 0
                
        
        for alphabet, frequencyOfAlphabet in sHashMap.items():
            if frequencyOfAlphabet>0:
                permuteStr += alphabet*frequencyOfAlphabet
        
        return permuteStr
        
        
        
        