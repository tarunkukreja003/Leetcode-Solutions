class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        [[1,3], [3,4]] -> [[1,4]]
        if start == end then it is overlapping
        start <= end
        
        can two intervals be same? - no
        
        are the intervals sorted by any start time or end time or any other parameter? - no
        
        [[1,1] [2,4]] -> [[1,1],[2,4]]
        
        
        [[1,10], [2,10]] -> [1,10]
        
        [[1,10], [2,5], [3,7]] -> [1,10]
        
        [[1,10]]
        
        
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        
        output = [[1,3]]
        
        let's sort the intervals arr by start time
        
        
        
        
       
        
        i points to latest non-overlapped interval in output list -> last interval in the outputNonOverlappedList
        j points to the current interval in intervals
        
    
        
        
        endi > startj -> overlapping
        
        endi == startj -> overlapping
        
        endi < startj -> not overlapping
        
        overlaps:
            if endi == startj:
                these are overlapped, start will not change, endi = endj for the current ouput array list
            elif endi > startj:
                start will not change, endi = max(endi, endj)
            
        not-overlapping:
            append the current interval j to output array and i will point to this non-overlapped array now
            
            
        
            
        
        
        
        """
        # overlapping intervals -> they have same start and end, start and end is intersecting, start and end is contained within another start and end -> if two intervals have any common integer(s) then they are overlapping
        # merge result -> if we merge 2 intervals the start will be of the smaller start number and the end will be the one which has bigger end integer
        
        # the result should contain all non-overlapping intervals
        
        if not intervals:
            return []
        
        # time complexity -> O(nlogn)
        
        # sort the intervals according to start
        
        intervals.sort(key=lambda x: x[0])
        mergedIntervalsList = [intervals[0]]
        
        # intervals are now sorted by start
        i = 1
        while i < len(intervals):
            # check for overlap with the already mergedIntervals
            # we only need to check the end of the last interval in mergedIntervals with start of the current - the advantage of sort
            if intervals[i][0] <= mergedIntervalsList[-1][1]:
                # overlap
                
                # find the mergedInterval in the mergedInterval set and update its end with the current interval's end
                
                # endi = max(endi, endj)
                mergedIntervalsList[-1][1] = max(intervals[i][1], mergedIntervalsList[-1][1])
                i += 1
            
            else:
                # not overlapping
                mergedIntervalsList.append(intervals[i])
                i += 1
        
        return mergedIntervalsList
                
                
                    
                
            
        