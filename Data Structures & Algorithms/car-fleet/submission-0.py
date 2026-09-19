class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [[position[i],speed[i]] for i in range(len(speed))]
        fleet.sort()

        stack = []

        for p,s in fleet[::-1]:
            t = (target - p)/s
            stack.append(t)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
            
        
        return len(stack)
        