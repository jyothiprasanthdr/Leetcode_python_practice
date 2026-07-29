class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        l,r=0, len(arr)-1
        res=-1
        while l<=r:

            m=(l+r)//2

            if m==len(arr)-1:
                return m

            if arr[m]>arr[m+1]:
                res=m
                r=m-1
            else:
                
                l=m+1
        return res