class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        
         4-directionally adjacent means just adjacent
        
        is it possible to have more than one rotten orange in the grid? - yes
        if all the cells are empty then? -> just return 0
        if there is a fresh orange which is unreachable/can't become rotten then return -1
        find the first rottoen orange
        
        
        
        
        this cannot be done via dfs because when we move to adjacent orange, minute will be incremented by 1 and then the the curr orange will move to its adjacent orange and minute will be incremented by 1, so in 1 dfs call only 1 fresh orange is rottened and minute is increased by 1 , so BFS is the approach we have to take here, since every minute all adjacent fresh oranges should be rottened
        
        
        
        2 1 0 0
        0 0 0 0
        0 1 2 0
        0 0 0 0
        1 2 0 0
        
        1 min
        
        
        [[(x2,y2),1], [(x3,y3),1], [(x4,y4),2]]
        
        we'll have levels, while q[0] has curr level -> pop the leftmost element and push their adjacent neighbors in the queue with level+1 
        
        for the curr level min += 1
        
        """
        
        # first check if there are any oranges at all, if all cells are empty just return 0
        orangesExistsInGrid = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    orangesExistsInGrid = True
        
        if not orangesExistsInGrid:
            return 0
                                        
        
        self.minimumMinutes = 0
        freshOrangesExists = False
        self.adjancentFreshOrnangeQueue = deque([])
        
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.adjancentFreshOrnangeQueue.append([(i,j),0])
                    
        def addElementsToQueue(level, row, col):
            isFreshOrangeAdjacent = False
            if row-1>=0 and grid[row-1][col] == 1:
                self.adjancentFreshOrnangeQueue.append([(row-1, col), level])
                grid[row-1][col] = 2
                isFreshOrangeAdjacent = True
            if row+1 < len(grid) and grid[row+1][col] == 1:
                self.adjancentFreshOrnangeQueue.append([(row+1, col), level])
                grid[row+1][col] = 2
                isFreshOrangeAdjacent = True
            if col-1 >=0 and grid[row][col-1] == 1:
                self.adjancentFreshOrnangeQueue.append([(row, col-1), level])
                grid[row][col-1] = 2
                isFreshOrangeAdjacent = True
            if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                self.adjancentFreshOrnangeQueue.append([(row, col+1), level])
                grid[row][col+1] = 2
                isFreshOrangeAdjacent = True
            
            return isFreshOrangeAdjacent
            
        while self.adjancentFreshOrnangeQueue:
            # all rotten oranges will be taken out together
            isFreshOrangeAdjacent = False
            indices, currLevel = self.adjancentFreshOrnangeQueue.popleft()
            isFreshOrangeAdjacent = addElementsToQueue(currLevel+1, indices[0], indices[1])
            print("indices: ", indices)
            print("currLevel: ", currLevel)
            
            while self.adjancentFreshOrnangeQueue and self.adjancentFreshOrnangeQueue[0][-1] == currLevel:
                indices, level = self.adjancentFreshOrnangeQueue.popleft()
                isFreshOrangeNeighbor = addElementsToQueue(level+1, indices[0], indices[1])
                if isFreshOrangeNeighbor:
                    isFreshOrangeAdjacent = True
                print("inside ")
                print("indices: ", indices)
                print("currLevel: ", level)
            
            if isFreshOrangeAdjacent:
                self.minimumMinutes += 1
            print("self.minimumMinutes: ", self.minimumMinutes)
            print("queue: ", self.adjancentFreshOrnangeQueue)
            
            
            
        
#         # if there are still some fresh oranges left then return -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOrangesExists = True
        
        if freshOrangesExists:
            return -1
        
        return self.minimumMinutes
        
        
        