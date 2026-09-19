class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {1:1,2:2}
        
        def ways(i):
            if i in mem:
                return mem[i]

            mem[i] = ways(i-1) + ways(i-2)
            return mem[i]
        
        return ways(n)