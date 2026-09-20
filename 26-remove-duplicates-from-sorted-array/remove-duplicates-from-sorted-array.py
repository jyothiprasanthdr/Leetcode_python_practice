class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        

        k=1
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[fast-1]:
                nums[k]=nums[fast]
                k+=1
        return k