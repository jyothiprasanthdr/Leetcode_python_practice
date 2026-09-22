class Solution:
    def maxArea(self, height: list[int]) -> int:

        res=0

        l=0
        r=len(height)-1

        while l<r:

            width= r-l
            h = min(height[l],height[r])

            water = width * h
            if res<water:
                 res=water
            if height[l]<height[r]:
                l+=1
            else:
                r=r-1
        return res




        