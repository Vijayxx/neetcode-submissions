class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        f = set()
        max_count = 0
        while r < len(s):
            if s[r] not in f:
                f.add(s[r])
                count  = len(f)
                max_count = max(max_count,count)
                r += 1
            else:
                while s[r] in f:
                    f.discard(s[l])
                    l+=1
            
        
        return max_count