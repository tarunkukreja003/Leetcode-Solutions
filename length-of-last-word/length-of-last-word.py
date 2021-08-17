class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        spaceAfterWordDetected = False
        letterDetectedFlag = False
        lastWord = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ' and spaceAfterWordDetected == False:
                lastWord += s[i]
                letterDetectedFlag = True
            
            if letterDetectedFlag == True and s[i] == ' ':
                spaceAfterWordDetected = True
        
        return len(lastWord)
                
        