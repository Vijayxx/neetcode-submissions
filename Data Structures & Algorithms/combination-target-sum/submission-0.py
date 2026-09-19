class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res ,path = [],[]
        total = 0

        def backtrack(i,total):
            if len(nums) == i or total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            path.append(nums[i])
            total += nums[i]
            backtrack(i,total)
            path.pop()
            
            backtrack(i+1,total-nums[i])

        backtrack(0,total)

        return res
