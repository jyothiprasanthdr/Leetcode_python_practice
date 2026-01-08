class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        sum=0
        res = 0
        for i in nums:
            sum += i
            if sum - k in prefixSum:
                res += prefixSum[sum - k]
            
            if sum not in prefixSum:
                prefixSum[sum] = 1
            else:
                prefixSum[sum] += 1

        return res

        
        