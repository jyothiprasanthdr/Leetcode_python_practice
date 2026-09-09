class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):

            days_needed=1
            current_weight=0    

            for w in weights:

                if current_weight+w>capacity:
                    days_needed+=1
                    current_weight=0

                current_weight+=w
            return days_needed<=days


        l=max(weights)
        r= sum(weights)

        ans = 0



        while l<=r:
                m = (l+r)//2

                if canShip(m):
                    ans=m
                    r=m-1
                else:
                    l=m+1

        return ans
