class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        q = deque()
        seen = set()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    fresh+=1


        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                d = [[r,c+1],[r+1,c],[r,c-1],[r-1,c]]
                for l,k in d:
                    if l < 0 or l >= n or k < 0 or k >= m or grid[l][k] != 1 or (l,k) in seen:
                        continue
                    q.append([l,k])
                    seen.add((l,k))
                    grid[l][k] = 2
                    fresh -= 1

            time += 1

        if fresh > 0:
            return -1
        
        return time
        

            
        
