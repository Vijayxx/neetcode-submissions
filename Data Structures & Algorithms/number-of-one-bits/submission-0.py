class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            c = n%2
            res += c
            n >>= 1
        
        return res