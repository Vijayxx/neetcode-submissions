class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(nums,index):

            if index == len(nums):
                res.append(path[:])
                return

            path.append(nums[index])
            backtrack(nums,index + 1)
            path.pop()

            backtrack(nums,index+1)          

        backtrack(nums,0)

        return res  