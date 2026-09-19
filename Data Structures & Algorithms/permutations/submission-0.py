class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res , per, chosen = [] , [] , [False]*len(nums)

        def backtrack(i):
            if i == len(nums):
                res.append(per[:])
                return
            
            for j in range(len(nums)):
                if not chosen[j]:
                    per.append(nums[j])
                    chosen[j] = True
                    backtrack(i+1)
                    per.pop()
                    chosen[j] = False

        
        backtrack(0)

        return res

