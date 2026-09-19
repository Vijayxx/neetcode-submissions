class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i in "+-/*":
                b = stack.pop()
                a = stack.pop()
                res = a+b if i =="+" else(a-b if i == "-" else(a*b if i == "*" else(int(a/b) if i == "/" else "")))
                stack.append(res)
            else:
                stack.append(int(i))

        return stack[-1] 
