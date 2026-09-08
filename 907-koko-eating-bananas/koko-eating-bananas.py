class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        ans=-1
        while l<=r:

            m = (l+r)//2

            if self.canFinish(piles, m,h):
                ans=m   
                r=m-1
            else:
                l=m+1
        return ans

    def canFinish(self, piles, m, h):

        t=0
        for p in piles:

            t+= math.ceil(p/m)
            if t >h:
                return False

            
        return t<=h
