class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        
        totalsum=sum(nums)
        leftsum=0
        for i, num in enumerate(nums):
            
            rightsum=totalsum-leftsum-nums[i]
            if rightsum==leftsum:
                return i
            leftsum+=num
        return -1
        