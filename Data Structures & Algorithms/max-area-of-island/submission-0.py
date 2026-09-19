class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r,c):
            d = [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]
            grid[r][c] = 0
            area = 1
            for i,j in d:
                if i < 0 or i >= n or j < 0 or j>=m or grid[i][j] == 0:
                    continue
                area += dfs(i,j)
            return area

            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area,area)
        
        return max_area