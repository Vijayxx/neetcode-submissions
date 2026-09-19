class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1

        maxw = 0
        while(l<r):
            water = min(heights[l],heights[r])*(r-l)
            if water > maxw:
                maxw = water
            
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1

        return maxw