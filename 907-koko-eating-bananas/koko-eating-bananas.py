class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(piles,h,k):
            hours=0
            for p in piles:

                hours += math.ceil(float(p/m))
            return hours<=h

        l,r= 1, max(piles)
        res =float(inf)
        while l<=r:

            m = (l+r)//2

            if can_eat(piles, h, m):

                res = min(res,m)
                r=m-1

            else:
                l=m+1
        return res

    



