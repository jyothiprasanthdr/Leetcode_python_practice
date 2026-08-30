class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l= self.BS(nums, target, True)
        r= self.BS(nums, target,False)
        return [l,r]



    
    def BS(self, nums, target,leftSide):
        l=0
        r=len(nums)-1
        i=-1
        while l<=r:

            m = (l+r)//2

            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                i=m
                if leftSide:
                    r=m-1
                else:
                    l=m+1
        return i 
        

        