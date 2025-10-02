class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
  
        last =-1
        def FirstIndex(nums,target):

            l , r = 0 , len(nums)-1
            first=-1
            
            while l <= r:

                m = (l+r)//2

                if nums[m] == target:
                    first = m
                    r=m-1
                
                elif nums[m] > target:
                    r=m-1
                
                else:
                    l = m+1
            return first


        def LastIndex(nums,target):

            l , r = 0 , len(nums)-1
            last=-1
            
            while l <= r:

                m = (l+r)//2

                if nums[m] == target:
                    last = m
                    l=m+1
                
                elif nums[m] > target:
                    r=m-1
                
                else:
                    l = m+1
            return last
        return [FirstIndex(nums,target),LastIndex(nums,target)]

       