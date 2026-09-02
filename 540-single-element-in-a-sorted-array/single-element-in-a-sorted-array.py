class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l=nums[0]

        for i in nums[1:]:
            l=l^i
        return l