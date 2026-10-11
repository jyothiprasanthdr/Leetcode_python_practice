class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix= defaultdict(int)
        prefix[0]=-1
        running_sum =0

        for i,num in enumerate(nums):
            running_sum += num
            remainder= running_sum %k
            if remainder  in prefix:
                if i - prefix[remainder] >=2:
                    return True
            else:
                prefix[running_sum%k]=i
        return False