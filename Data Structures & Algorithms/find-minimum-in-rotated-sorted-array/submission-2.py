class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[r] < nums[m]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            else:
                return nums[m]
