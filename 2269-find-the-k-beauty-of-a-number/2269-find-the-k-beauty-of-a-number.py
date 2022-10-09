class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        """
        
        if the substring contains all 0's then just continue
        
        240 k = 2
        
        
        sliding window
        2  4  0
           ----
        newStr = strOfLengthK - strOfLengthK[i] + strOfLengthK[i+k]
        
        
        one more thing:
        if substr  = "0020" then strip the leading zeroes
        """
        
        self.k_beauty = 0
        # convert num to str
        wholeNumStr = str(num)
        n = len(wholeNumStr)
        
        if k > n:
            return 0
        
        # no need of removing the leading zeores from string, if we do int(string), it will remove all the leading zeroes, if they are all zeroes then one 0 will be left in int(string)
        
        def convertToIntAndCheckDivisor(string):
            
            integer = int(string)
            print("integer", integer)
            if integer !=0 and num % integer == 0:
                self.k_beauty += 1

        
        for j in range(n-k+1):
            newStr = wholeNumStr[j:j+k]
            print(newStr)
            convertToIntAndCheckDivisor(newStr)
        
        return self.k_beauty
            
            
        
        
        