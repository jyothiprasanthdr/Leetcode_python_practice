class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]

       
        n=len(nums)
        res = [-1]*n


        for i in range(n*2):

            while stack and nums[stack[-1]] <nums[i%n]:

                ind = stack.pop()
                res[ind]=nums[i%n]
            if i<n:
                stack.append(i)
        return res