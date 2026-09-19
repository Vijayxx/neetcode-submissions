class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = defaultdict(list)
        for i,j in prerequisites:
            adj[j].append(i)

        result = []
        completed = set()
        path = set()
        
        def dfs(i):
            if i in path:
                return False
            if i in completed:
                return True
            path.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            completed.add(i)
            result.append(i)
            return True

        for i in range(n):
            if not dfs(i):
                return []

        return result[::-1]
        
