class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def recurse(i, j):
            if i == m-1 and j == n-1: return grid[i][j]
            try:
                return grid[i][j] + min(recurse(i+1, j), recurse(i, j+1))
            except:
                return float('inf')
        
        return recurse(0, 0)