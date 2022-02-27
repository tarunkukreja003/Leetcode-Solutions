class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        if there are no rotten oranges then there will be all fresh oranges, hence we'll return -1
        
        what directly comes to our mind is that we'll use BFS to solve this problem
        
        first we'll store all the rotten oranges at 0th minute in the queue(their indices)
        
        
        when we pop a rotten orange from the queue we'll first increment the minute by 1
        
        now all the fresh oranges adjacent to the popped orange will become rotten and we'll put all of them in the queue
        
        we'll run the algorithm until the queue is not empty
        
        time complexity -> O(mn)
        space complexity -> O(mn)
        
        
        x o o 
        o o o
        o o x
        
        """
        n = len(grid)
        m = len(grid[0])
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        queue = collections.deque([])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        minutes = 0
        while queue:
            rowRotten, colRotten, minute = queue.popleft()
            minutes = minute
            for direction in directions:
                r = rowRotten + direction[0]
                c = colRotten + direction[1]
                
                if r>=n or c >= m or r < 0 or c < 0 or grid[r][c] != 1:
                    continue
                queue.append((r,c,minute+1))
                grid[r][c] = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        
        return minutes
                    
        
        
        