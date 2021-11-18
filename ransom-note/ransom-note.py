class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineFreqCounter = {}
        
        for char in magazine:
            if char not in magazineFreqCounter:
                magazineFreqCounter[char] = 1
            else:
                magazineFreqCounter[char] += 1
        
        for char in ransomNote:
            print(magazineFreqCounter)
            if char in magazineFreqCounter and magazineFreqCounter[char] > 0:
                magazineFreqCounter[char] -= 1
            else:
                return False
        return True
        