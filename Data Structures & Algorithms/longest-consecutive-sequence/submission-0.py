class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        start = []

        for i in numset:
            if i-1 not in numset:
                start.append(i)
        
        maxcount = 0
        for i in start:
            curr = i
            count = 1

            while curr + 1 in numset:
                curr += 1
                count += 1
            
            maxcount = max(count,maxcount)
        
        return maxcount


            
