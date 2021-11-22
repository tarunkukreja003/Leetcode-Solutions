class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
        
        
        def checkPalindrome(s):
            # two pointer approach
            i, j = 0, len(s) - 1
            while i<=j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
                
            return True
        
        s = ''.join(filter(str.isalnum,s))
        s = s.lower()
        print(s)
        
        return checkPalindrome(s)
        # convert str to lowercase, remove spaces, alphanumeric digits, letters
                