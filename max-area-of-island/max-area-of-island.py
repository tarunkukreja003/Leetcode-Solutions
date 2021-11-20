class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visitedLand = set()
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visitedLand.add((r,c))
            area = 1
            
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions: 

                    nextRow, nextCol = row + dr, col + dc

                    if nextRow in range(rows) and nextCol in range(cols) and grid[nextRow][nextCol] == 1 and (nextRow, nextCol) not in visitedLand:
                        q.append((nextRow,nextCol))
                        visitedLand.add((nextRow, nextCol))
                        area += 1

            return area
            
            
            
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1 and (r,c) not in visitedLand:
                    area = bfs(r,c)
                    
                    if maxArea < area:
                        maxArea = area
                        
        return maxArea            
        