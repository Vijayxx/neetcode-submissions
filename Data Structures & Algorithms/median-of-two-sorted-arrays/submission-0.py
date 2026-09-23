class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        total = len(a) + len(b)
        half = total //2
        if len(b) < len(a):
            a,b=b,a
        l, r = 0, len(a) - 1
        while True:
            m = (l+r)//2
            n = half - m - 2
            al = a[m] if m >= 0 else float("-infinity")
            ar = a[m+1] if m+1 < len(a) else float("infinity")
            bl = b[n] if n >= 0 else float("-infinity")
            br = b[n+1] if n+1 < len(b) else float("infinity")
            if al > br:
                r = m-1
            elif bl > ar:
                l = m+1
            else:
                if total%2 == 0:
                    return (max(al,bl) + min(ar,br))/2
                else:
                    return min(ar,br)
        

