class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height)-1
        area= -1
        while l<=r:
            
            if height[l] > height[r]:
                area=  max(area,height[r] * (r-l))
                r-=1
            else:
                area=  max(area,height[l] * (r-l))
                l+=1
            
           
        return area


            
        