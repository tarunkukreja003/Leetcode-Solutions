class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        """
        "bcaba" -> possible outputs = [bca, cab]
        
        
        
        
        
        
        "cbacdcbc" -> "acdb"
        
        "baab" -> "ab"
        
        "baba" -> "ab"
        
        ""
        
        we are going to use recursion
        
        we basically have to find the leftmost characters
        leftmost chracter means its the smallest character such that suffix of it contains every other letter in the string atleast once
        
        once the iteration ends we have the pos of smallest char, but char may appear later in the string str[pos:], so delete it from the remaining string
        
        c = Counter(s)
        def recursiveStr(s):
            pos = 0
            
            
            
            for i in range(len(s)):
                
                # pos calculates the smallest char in s
                if s[i] < s[pos]:
                    pos = i
                
                # if the curr element is not available afterwards then break the curr iteration and you have the pos
                
                c[s[i]] -= 1
                
                if c[s[i]] == 0:
                    break
            delete the pos from counter
            return s[pos] + recursiveStr(s[pos:].replace(s[pos], ""))

        
        time complexity -> in every recursive call an alphabet's all occurrences are being removed, so at max we'll have 26 recusion calls
        
        and hashmap takes O(n) time to build
        
        space complexity -> O(n) * 26 -> recursion stack(26)
        
        
        """
        
        
        def recursiveStr(s):
            # everytime we'll have to make frequency counter because frequency of characters occuring after pos has also been changed in the pervious iteration
            
            c = collections.Counter(s)
            pos = 0
            
            for i in range(len(s)):
                
                # pos calculates the smallest char in s
                if s[i] < s[pos]:
                    pos = i
                
                # if the curr element is not available afterwards then break the curr iteration and you have the pos
                
                c[s[i]] -= 1
                
                if c[s[i]] <= 0:
                    break
            
            
            if pos < len(s) and s[pos] in c:
                c.pop(s[pos], None)
            
            return s[pos] + recursiveStr(s[pos+1:].replace(s[pos], "")) if s else ''
        
        
        return recursiveStr(s)   
        
        
        
                
        
        
        
        
        