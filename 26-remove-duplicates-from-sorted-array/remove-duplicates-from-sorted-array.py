class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        fast = slow = 0

        while fast <= len(nums)-1:

            if nums[fast]!= nums[slow]:
                slow+=1
                nums[slow]= nums[fast]
                
            fast+=1
            
        return slow+1
        