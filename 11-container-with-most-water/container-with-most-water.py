class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_water=0
        while l<r:
            
            trapped= (r-l) * min(height[l],height[r])
            if max_water < trapped:
                max_water=trapped
                
            if height[l]<= height[r]:
                l+=1
            else:
                r-=1
        return max_water