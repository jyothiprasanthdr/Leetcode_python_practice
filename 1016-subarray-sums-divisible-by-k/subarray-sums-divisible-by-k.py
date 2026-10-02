class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        prefix_cnt =defaultdict(int)
        prefix_cnt[0]=1 

        totalsum = 0
        count=0
        for i, num in enumerate(nums):

            totalsum+= num
            rem = totalsum % k
            if rem in prefix_cnt:
                
                count+= prefix_cnt[rem]
            prefix_cnt[rem]+=1
        return count

        