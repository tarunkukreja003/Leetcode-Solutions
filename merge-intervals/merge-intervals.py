class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # overlapping intervals -> they have same start and end, start and end is intersecting, start and end is contained within another start and end -> if two intervals have any common integer(s) then they are overlapping
        # merge result -> if we merge 2 intervals the start will be of the smaller start number and the end will be the one which has bigger end integer
        
        # the result should contain all non-overlapping intervals
        
        if not intervals:
            return []
        
        # [[2,6],[5,8],[10,11],[11,12]]
        
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
                if intervals[i][1] > mergedIntervalsList[-1][1]:
                    mergedIntervalsList[-1][1] = intervals[i][1]
                    i += 1
                    
                else:
                    # interval fully contained
                    i += 1
            
            else:
                # not overlapping
                mergedIntervalsList.append(intervals[i])
                i += 1
        
        return mergedIntervalsList
                
                
                    
                
            
        