import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for x,y in points:
            dist = x**2 + y**2
            l.append((dist,[x,y]))
        heapq.heapify(l)
        print(l)
        result = []
        for i in range(k):
            result.append(heapq.heappop(l)[1])
        return result

        
        
        
        