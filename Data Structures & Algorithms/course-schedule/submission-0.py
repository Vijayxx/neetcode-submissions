class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = defaultdict(list)
        for i,j in prerequisites:
            adj[j].append(i)

        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            visited.add(i)
            return True
            
        path = set()
        visited = set()

        for i in range(n):
            if not dfs(i):
                return False
        
        return True