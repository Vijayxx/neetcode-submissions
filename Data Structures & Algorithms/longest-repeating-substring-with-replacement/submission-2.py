class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        maxlen = 0
        while r < len(s):
            d = {}
            for i in s[l:r+1]:
                d[i] = 0
            for i in s[l:r+1]:
                d[i] += 1
            if (r - l+1) - max(0,max(d.values())) <= k:
                maxlen = max(maxlen,r - l + 1)
                r+=1
            else:
                l+=1
        
        return maxlen
        
        
        

            