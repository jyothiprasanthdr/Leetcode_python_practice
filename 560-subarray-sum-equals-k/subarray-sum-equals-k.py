class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum ={0:1}
        curr_sum =0
        count=0

        for i in range(len(nums)):
            curr_sum +=nums[i]
            complement= curr_sum - k
            if complement in prefix_sum:
                count+= prefix_sum[complement]

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0)+1
        return count

        
        