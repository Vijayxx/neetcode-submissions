class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,sub = [], []
        op, cl = 0 , 0

        def backtrack(op, cl):
            if op == cl == n:
                res.append("".join(sub))
                return
            
            if op < n:
                sub.append("(")
                backtrack(op +1, cl)
                sub.pop()
            
            if cl < op:
                sub.append(")")
                backtrack(op,cl+1)
                sub.pop()
        
        backtrack(0,0)

        return res
                
            