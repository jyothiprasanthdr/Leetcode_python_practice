class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x ==1 or x==0:
            return x

        l =1
        r=x
        res=0
        while l<=r:

            m = (l+r)//2

            if m*m <=x :
               l=m+1
               res=m
            else:
                r=m-1

       
                
        return res
        