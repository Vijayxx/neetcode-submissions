class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        s = set()

        for i in range(len(nums)):
            s.add(nums[i])
            h[nums[i]] = 0
        
        for i in range(len(nums)):
            if nums[i] in s:
                h[nums[i]]+=1

        h = dict(sorted(h.items(),key = lambda item : item[1], reverse = True))
        
        a = list(h.keys())

        a = a[:k]

        return a