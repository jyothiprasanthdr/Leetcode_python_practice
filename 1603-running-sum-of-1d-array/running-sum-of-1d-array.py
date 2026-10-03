class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        for i, num in enumerate(nums):

            if i>0:
                nums[i]+=nums[i-1]

        return nums
        