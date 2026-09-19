class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        i = len(temperatures) -1
        while i >= 0:
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1] - i

            stack.append(i)
            i-=1
            
        print(stack)
        return result
                

            
            