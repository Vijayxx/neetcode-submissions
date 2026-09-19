class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        count = 0
        farthest = 0
        currend = 0

        for i in range(n-1):
            farthest = max(farthest,nums[i] + i)

            if i == currend:
                currend = farthest
                count += 1

        return count
