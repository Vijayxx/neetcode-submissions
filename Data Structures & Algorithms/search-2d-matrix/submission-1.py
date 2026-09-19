class Solution:
    def searchMatrix(self,matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m*n - 1

        def search2d(l,r):
            if l > r:
                return False
            
            mid = (l+r)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return search2d(l,mid - 1)
            else:
                return search2d(mid+1,r)
        
        return search2d(l,r)
