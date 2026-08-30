class Solution:
    def findPeakElement(self, arr: List[int]) -> int:

        l=0
        r=len(arr)-1
        ans=-1

        while l<=r:

            m = (l+r)//2

            if m==len(arr)-1:
                return m
            
            if arr[m]>arr[m+1]:
                ans=m
                r=m-1
            else:
                l=m+1

        return ans
       