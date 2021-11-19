class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we'll first be using BFS
        # we'll traverse the whole grid
        # if the current element is 1 and is not visited then perform dfs on it
        # after this island ++
        
        ## dfs function - in dfs we'll be looking at top, bottom, left of the current element
        # if any of the neighbors is 1 then dfs to that and just keep marking visited
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visitedLand = set()
        numberOfIslands = 0
        
        
        def dfs(r,c):
            visitedLand.add((r,c))
            
            
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            
            for dr, dc in directions:
                nextRow, nextCol = r + dr, c + dc
                
                if nextRow in range(rows) and nextCol in range(cols) and grid[nextRow][nextCol] == "1" and (nextRow, nextCol) not in visitedLand:
                    dfs(nextRow, nextCol)
                
                
                
                
                
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visitedLand:
                    dfs(r, c)
                    numberOfIslands += 1
        
        return numberOfIslands
                
                