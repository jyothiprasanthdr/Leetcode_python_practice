class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l , r = 0 , k-1
        max_sum= sum(nums[l:k]) 
        max_avg = max_sum/k

        while r <len(nums)-1:

          
            max_sum = max_sum + nums[r+1]-nums[l]   
            max_avg = max(max_avg,max_sum/k )  
            l+=1
            r+=1
        return max_avg