class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l=0
        r=len(arr)-1

        while l<=r:

            m = (l+r)//2

            if arr[m]==target:
                return m
            if arr[l]<=arr[m]:

                if target < arr[l] or target> arr[m]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target>arr[r] or target <arr[m]:
                    r=m-1
                else:
                    l=m+1
        return -1

                
               