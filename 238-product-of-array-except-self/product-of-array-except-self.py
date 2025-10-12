class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length= len(nums)
        res= [1] * length
        left =1

        for i in range(length):

            res[i] *= left
            left*= nums[i]

        right =1
        for i in reversed(range(length)):
            res[i] *=right
            right*= nums[i]
        return res