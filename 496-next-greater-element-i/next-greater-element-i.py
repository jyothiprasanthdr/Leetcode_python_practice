class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]

        res = [-1]*len(nums1)
        ans={ n:i for i,n in enumerate(nums1)}

        for i, num in enumerate(nums2):

            while stack and stack[-1]<=num:
                    n=stack.pop()
                    ind=ans[n]
                    res[ind]=num

            if num in ans:
                stack.append(num)
        return res