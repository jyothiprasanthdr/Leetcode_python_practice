class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r =0 , len(nums)-1
        last= nums[r]
        res= float('inf')

        while l<=r:
            m = (l+r)//2
            
            
            if nums[m] > last:
                l=m+1
            elif nums[m]<=last:
                res= min(res,nums[m])
                r=m-1

        return res