class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

            prefix = {0:1}
            curr_sum =0
            count = 0 

            for i in range(len(nums)):
                curr_sum += nums[i]
                complement = curr_sum - k
                if complement in prefix:
                    count += prefix[complement]
                prefix[curr_sum] = prefix.get(curr_sum,0)+1
            return count
        
        