class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmin = nums[0]
        curmax = nums[0]
        maxsum = nums[0]

        for i in range(1,len(nums)):
            oldmin= curmin
            oldmax = curmax
            curmax = max(curmax+nums[i], nums[i],oldmin+nums[i])
            curmin = max(curmin+nums[i], nums[i], oldmax+nums[i])
            maxsum = max(maxsum,curmax)

        return maxsum