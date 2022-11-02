class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        
        [[1]] -> 1
        [[1,1]] -> 1
        [[1,0,1]] -> 2
        
        if 1 is on 1st row then above it is water
        
        find the first 1 then do dfs from there
        """
        
        self.visited = set()
        self.numberOfIslands = 0
        
        def dfs(row, col):
            
            # check all 4 sides
            self.visited.add((row,col))
            if row-1 >= 0 and grid[row-1][col] == "1" and (row-1, col) not in self.visited:
                dfs(row-1, col)
                
            if row+1 < len(grid) and grid[row+1][col] == "1" and (row+1, col) not in self.visited:
                dfs(row+1, col)
            if col-1 >= 0 and grid[row][col-1] == "1" and (row, col-1) not in self.visited:
                dfs(row, col-1)
            
            if col+1 < len(grid[0]) and grid[row][col+1] == "1" and (row, col+1) not in self.visited:
                dfs(row, col+1)
            
            
            # check all 4 sides for water
            
            
                
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and grid[i][j] == "1":
                    dfs(i,j)
                    
                    # for every connected chain of dfs there will be 1 island 
                    self.numberOfIslands += 1
        
        return self.numberOfIslands
        
        