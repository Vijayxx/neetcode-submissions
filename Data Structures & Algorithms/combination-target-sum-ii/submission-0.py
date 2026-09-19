class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []
        total = 0

        def backtrack(i,total):
            if total == target:
                res.append(path[:])
                return
            if i == len(candidates) or total>target:
                return
            
            path.append(candidates[i])
            backtrack(i+1,total+candidates[i])
            path.pop()

            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j,total)
        
        backtrack(0,total)

        return res