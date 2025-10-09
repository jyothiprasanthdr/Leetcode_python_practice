class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l , r = 0 , k-1
        max_sum= wind_sum=sum(nums[l:k]) 
     

        while r <len(nums)-1:
      
            
            wind_sum = wind_sum + nums[r+1]-nums[l]
            max_sum= max(max_sum, wind_sum)
            l+=1
            r+=1
        return max_sum/k