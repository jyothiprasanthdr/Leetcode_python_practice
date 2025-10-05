class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r= 0, len(arr)-1
        peak=-1

        while l<=r:

            m = (l+r)//2
            if arr[m] > arr[m+1]:
                peak=m
                r=m-1
            else:
                l=m+1
        return peak