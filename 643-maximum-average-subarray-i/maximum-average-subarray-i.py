class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window_sum =0
        max_avg=float('-inf')
        left =0
        for right in range(len(nums)):

            window_sum+=nums[right]

            if right >= k -1:
                
                 max_avg= max(max_avg, window_sum/k)
                 window_sum -=nums[left]
                 left+=1
        return max_avg

