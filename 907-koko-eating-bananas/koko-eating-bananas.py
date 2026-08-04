class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res=-1
        while l<=r:

            m= l+ (r-l)//2

            if self.feasible(m, piles, h):
                res=m
                r=m-1
            else:
                l=m+1
    
        return res

    def feasible(self,k, piles, h):
        
        time=0
        for p in piles:    
                time+= math.ceil(p/k)
                if time >h:
                    return False
     
        return time <=h
    
