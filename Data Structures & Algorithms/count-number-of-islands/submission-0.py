class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n , m = len(grid), len(grid[0])
        seen = {}
        no = 0
        def dfs(r,c):
            d = [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]
            grid[r][c] = "0"
            for p,q in d:
                if p >= n or p < 0 or q >= m or q < 0 or grid[p][q] == "0":
                    continue
                dfs(p,q)


        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r,c)
                    no +=1

        return no

            