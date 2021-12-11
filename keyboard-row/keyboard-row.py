class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # words = ["vjnfrjvn", "njurnj"]
        # can the characters in the string be alphanumeric like whitespace, punctuation, number - no
        # is the american keyboard given to us in the array? - your choice 
        
        # Brute force complexity will be 
        # length of word 1 * (length of characters in row 1 + length of characters in row 2 + length of characters in row 3  ) + length of word 2 * (length of characters in row 1 + length of characters in row 2 + length of characters in row 3  ) ... +  length of word n * (length of characters in row 1 + length of characters in row 2 + length of characters in row 3  ) ...
        
        
        # a better approach would be to store keyboard rows into hashmap and they will have a value of their row
        
        wordsInOneRow = []
        
        keyboardRowHashMap = {
            1:"qwertyuiop",
            2:"asdfghjkl",
            3:"zxcvbnm"
            }
        
        
        
        for word in words:
            wordLower = word.lower()
            rowNumber = 0
            count = 0            
            for key, value in keyboardRowHashMap.items():
                if wordLower[0] in value:
                    rowNumber = key
            
            for char in wordLower:
                if char not in keyboardRowHashMap[rowNumber]:
                    break
        
                else:
                    count += 1
                    
            if count == len(word):
                wordsInOneRow.append(word)
        
        return wordsInOneRow
                    
        
        
        