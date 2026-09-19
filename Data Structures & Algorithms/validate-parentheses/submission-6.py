class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) %2 != 0:
            return False
        for i in s :
            if i in "([{":
                stack.append(i)
            elif i == ")":
                if len(stack) == 0: return False

                if stack[len(stack)-1] != "(":
                    return False
                else:
                    stack.pop()
            elif i == "]":
                if len(stack) == 0: return False
                if stack[len(stack)-1] != "[":
                    return False
                else:
                    stack.pop()
            elif i == "}":
                if len(stack) == 0: return False

                if stack[len(stack)-1] != "{":
                    return False
                else:
                    stack.pop()
        result = True if len(stack) == 0 else False
        return result
            