class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = nums[0]
        curmin = nums[0]
        maxprod = nums[0]
        n = len(nums)

        for i in range(1,n):
            oldmax = curmax
            oldmin = curmin
            curmax = max(curmax*nums[i],nums[i],oldmin*nums[i])
            curmin = min(curmin*nums[i],nums[i],oldmax*nums[i])
            maxprod = max(curmax,maxprod)
        
        return maxprod