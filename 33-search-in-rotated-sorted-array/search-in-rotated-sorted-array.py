class Solution:
    def search(self, arr: List[int], target: int) -> int:

        l,r= 0, len(arr)-1

        while l<=r:

            m = (l+r)//2

            if arr[m]==target:
                return m

            if arr[l]<= arr[m]: # left sorted side

                if target > arr[m] or target < arr[l]:
                    l=m+1
                else:
                    r=m-1
            else:

                if target > arr[r] or target < arr[m]:
                    r=m-1
                else:
                    l=m+1
        return -1
        