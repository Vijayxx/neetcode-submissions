import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-i for i in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x  = -heapq.heappop(s)
            y  = -heapq.heappop(s)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(s,-(y-x))
            else:
                heapq.heappush(s,-(x-y))
        return -s[0] if s else 0
