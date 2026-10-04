class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_cnt= {0:-1}
        max_len=0
        prefixSum=0

        for i,n in enumerate(nums):
            
            prefixSum+= 1 if n==1 else -1
            if prefixSum in prefix_cnt:
                max_len=max(max_len, i- prefix_cnt[prefixSum])

            else:
                prefix_cnt[prefixSum]=i
        return max_len            