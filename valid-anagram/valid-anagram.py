class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if s and t are not of the same length then they cannot be anagrams
        s_length = len(s)
        t_length = len(t)
        
        if s_length != t_length:
            return False

        s_frequency_counter_dict = {}
        
        for letter in s:
            if letter in s_frequency_counter_dict:
                s_frequency_counter_dict[letter] += 1
            else:
                s_frequency_counter_dict[letter] = 1
        
        
        for letter in t:
            if letter in s_frequency_counter_dict:
                if s_frequency_counter_dict[letter] > 0:
                    s_frequency_counter_dict[letter] -= 1   
                else:
                    return False
            else:
                return False
        
        for frequency in s_frequency_counter_dict.values():
            if frequency > 0:
                return False
        
        return True
            
        