class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        d = {}
        for i in s1:
            d[i] = 0
        for i in s1:
            d[i] += 1
        result = False
        while r < len(s2):
            s = {}
            for i in s2[l:r+1]:
                s[i] = 0
            for i in s2[l:r+1]:
                s[i] += 1
            if s==d:
                result = True
            r += 1
            l += 1

        return result