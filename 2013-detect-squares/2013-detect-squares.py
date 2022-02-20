class DetectSquares:
    
    """
    https://leetcode.com/problems/detect-squares/discuss/1471914/Python-short-two-dictionaries-solution.
    
    """

    def __init__(self):
        """
        hash table data structure because we need to search for points and for duplicate points are allowed and should be treated as different points -> we can maintain the frequency of those points
        
        """
        self.frequencyCountDict = collections.Counter()
        self.xToYMapping = collections.defaultdict(Counter)
        
        

    def add(self, point: List[int]) -> None:
        """
        if already there in the hash table just increase its frequency
        """
        
        x,y = point
        self.frequencyCountDict[x,y] += 1
        self.xToYMapping[x][y] += 1
        
        

    def count(self, point: List[int]) -> int:
        """
        can the square edges touch the x-axis and y-axis? - yes
        
        area cannot be 0
        
        if the query point is in hash table don't use it
        
        axis-aligned square
        
        [11,10] -> in order for this to form an axis-aligned square there should be two points one having the same y-coordinate as of query point , one having the same x-coordinate as query point and the third point should have both points equal to x and y coordinate of the 2 points
        
        [5,5] -> query point
        
        [5,-5]  -> 1st point
        [-5,5] -> 2nd point
        [-5,-5] -> 3rd point
        
        {
        [2,10]:1
        [11,19]
        [2,19]
        
        }
        
        once the three points have been calculated put them in a set
        
        the set will contain unique frozensets of 3 points which have already been considered
        
        
        
        in the query point [x,y]
        
        if we have to form a square with 3 more points
        2 points will be [x,y2] and [x2,y] and the third point will be [x2,y2]
        
        we'll create a counter dictionary to store the count of points
        -> let's say three points have already been used to make the square with the query point, if those 3 points have frequency of 2 then the number of sqaures formed using those 3 points will be 2 
        
        we'll create a nested dictionary for every x there will be a list of y
        we shouldn't create a list as the value of dictionary because if we have duplicate y's we'll iterate over the same y multiple times and for every x,y we are counting the number of ways, so that x,y will be counted multiple times
        
        query point = [x,y]
        we can't use the same x,y
        {
        
        x : [
          y1, 
          y2,
          y,
          y3,
        ]
        }
        
        x,y2
        
        
        
        edge length = y2-y or y-y2
        
        numberOfWays += counterDict[x,y2] * counterDict[x + y2-y,y] * counterDict[x + y2-y,y2]
        numberOfWays += counterDict[x,y2] * counterDict[x + y-y2,y] * counterDict[x + y-y2,y2]
        
        
        for y2 in xDict[x]:
            if y == y2:
                continue
            
            
        
        
        
        
        """
        queryPoint = point
        x,y = queryPoint
        numberOfWays = 0
        
        for y2 in self.xToYMapping[x]:
            if y2 == y:
                continue
            
            numberOfWays +=  self.frequencyCountDict[x,y2] * self.frequencyCountDict[x+y2-y,y] * self.frequencyCountDict[x+y2-y,y2]
            numberOfWays +=  self.frequencyCountDict[x,y2] * self.frequencyCountDict[x+y-y2,y] * self.frequencyCountDict[x+y-y2,y2]
        
        return numberOfWays
            
        
        
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)