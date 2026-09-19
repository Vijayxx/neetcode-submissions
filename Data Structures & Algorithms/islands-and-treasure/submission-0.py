class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n , m = len(grid), len(grid[0])

        seen = set()
        qu = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    qu.append([i,j])
                    seen.add((i,j))
        
        dist = 0
        while qu:
            for i in range(len(qu)):
                r,c = qu.popleft()
                grid[r][c] = dist
                d = [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]
                for p,q in d:
                    if p < 0 or p == n or q < 0 or q >= m or grid[p][q] == -1 or (p,q) in seen:
                        continue
                    seen.add((p,q))
                    qu.append([p,q])
            dist += 1

        