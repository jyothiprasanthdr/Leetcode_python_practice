class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}
        prefixsum=0
        max_length=0

        for i, num in enumerate(nums):

            prefixsum+= 1 if num==1 else -1
            if prefixsum in seen:
                max_length= max(max_length, i- seen[prefixsum])
            else:
                seen[prefixsum]=i
        return max_length