class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {(n,amount):0}
        
        def dfs(i,target):
            if target == amount:
                return 0
            if i == n and target < amount:
                return float("inf")
            take = float("inf")
            if (i,target) in memo:
                return memo[(i,target)]
            if target + coins[i] <= amount:
                take = 1 + dfs(i,target+coins[i])
            
            skip = dfs(i+1,target)

            memo[(i,target)] = min(take,skip)
            return memo[(i,target)]

        l = dfs(0,0)
        return -1 if l == float("inf") else l

