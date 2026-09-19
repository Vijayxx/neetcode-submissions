class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {(n,-1):0}

        def dfs(i,lastInd):
            if i == n:
                return 0
            if (i,lastInd) in memo:
                return memo[(i,lastInd)]
            take = 0
            if nums[i] > nums[lastInd] or lastInd == -1:
                take = 1 + dfs(i+1,i)
            skip = dfs(i+1,lastInd)
            memo[(i,lastInd)] =  max(take,skip)
            return memo[(i,lastInd)]
        
        return dfs(0,-1)