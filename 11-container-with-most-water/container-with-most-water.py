class Solution:
    def maxArea(self, height: list[int]) -> int:

        l=0
        r=len(height)-1
        amount=0
        
        while l<=r:

                amount= max(amount, min(height[l],height[r])*(r-l))
                
                if height[l]<height[r]:
                    l+=1
                else:
                    r-=1
        return amount
