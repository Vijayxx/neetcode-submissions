class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res , sub = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()

            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            backtrack(j)

        backtrack(0)

        return res