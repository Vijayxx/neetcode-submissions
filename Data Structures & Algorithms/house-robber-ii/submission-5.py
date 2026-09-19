class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
    
        def f(start,end):
            dp = [0]*(n+2)

            for i in range(end , start-1, -1):
                dp[i] = max(dp[i+1],dp[i+2]+nums[i])
            
            return dp[start]
            
        return max(f(1,n -1),f(0,n-2))