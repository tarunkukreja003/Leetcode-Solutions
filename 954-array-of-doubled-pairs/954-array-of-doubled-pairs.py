class Solution:
    """
    [1,2,4,16,8,4]
    
    [1,2,4,4,8,16]

    [1,2]
    
    
    in sort -4 should come after -2
    so we need to sort using abs as key
    
    [-2,2,-4,4]
    
    """
    def canReorderDoubled(self, arr: List[int]) -> bool:
        frequencyCounter = collections.Counter(arr)
        
        for element in sorted(arr, key = abs):
            # if the current element is used and does not have any frequncy left then continue
            # because it is double of some previous elements and has been used
            
            if frequencyCounter[element] == 0:
                continue
            # element in frequencyCounter and frequencyCounter[element] > 0 and 
            if frequencyCounter[2*element] == 0:
                return False
            
            
            frequencyCounter[element] -= 1
            frequencyCounter[2*element] -= 1
                
        
        return True
        
        