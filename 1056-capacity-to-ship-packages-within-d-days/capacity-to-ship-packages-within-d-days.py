class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r =max(weights), sum(weights)

        res=r

        while l<=r:

            m = l + (r-l)//2

            if self.feasible(weights, days, m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
    
    def feasible(self, weights, d, cap):

        days_needed=1
        current_weight=0
        for w in weights:

            if current_weight + w >cap:
                days_needed+=1
                current_weight=w
            else:
                current_weight+=w
        
            if days_needed>d:
                return False
        return True

        