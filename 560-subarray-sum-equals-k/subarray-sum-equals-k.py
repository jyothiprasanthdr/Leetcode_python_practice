class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1}
        currentsum=0
        count=0
        for num in nums:
            
            currentsum+=num
            diff = currentsum-k
            count+=prefix.get(diff,0)
            prefix[currentsum]=1+prefix.get(currentsum,0)
        return count