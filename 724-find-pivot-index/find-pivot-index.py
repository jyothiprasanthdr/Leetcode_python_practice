class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        leftsum=0

        for i,num in enumerate(nums):

            rightsum= total_sum - leftsum-num

            if leftsum==rightsum:
                return i
            leftsum+=num
        return -1        