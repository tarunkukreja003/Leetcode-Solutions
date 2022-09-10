class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        
        """
        is timeSeries sorted -> yes 
        t = 5
        duration = 3
        
        [5, 8 - 1] = [5,7] 
        
        t = 6
        [6,6+3-1] = [6,8]
        
        total time poisoned = 1 + 2 = 3
        
        
        time = [1,4] dur = 2
        
        t = 1 [1,1+2-1] = [1,2] -> 
        
        next element in timeSeries is not overlapping
        so
        inclusive so 2-1 + 1 = 2
        
        t = 4 [4,4+2-1] = [4,5] -> inclusive so 5-4 + 1 = 2
        
        total 4 sec
        
        -------------------------------
        time = [1] duration = 2
        
        finalInterval = [1,2]
        totalPoisonTime = 2
        
        ----------------------------
        algo
        
        
                
                
        
        """
        
        i = 1
        
        finalInterval = [timeSeries[0], timeSeries[0] + duration - 1]
        totalPoisonTime = 0
        
        while i < len(timeSeries):
            
            if finalInterval[1] >= timeSeries[i]:
                finalInterval[1] = timeSeries[i] + duration-1
                i += 1
            else:
                totalPoisonTime += finalInterval[1] - finalInterval[0] + 1
                finalInterval = [timeSeries[i], timeSeries[i] + duration - 1]
                i += 1
        
        totalPoisonTime += finalInterval[1] - finalInterval[0] + 1
        
        
        return totalPoisonTime
        