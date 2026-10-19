class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
            stack = []
            res=[-1]* len(nums1)
            ind_map={ n:i for i,n in enumerate(nums1)}

            for i,val in enumerate(nums2):

                while stack and stack[-1] < val:

                    prev_val = stack.pop()
                    ind= ind_map[prev_val]
                    res[ind]=val
                if val in nums1:
                    stack.append(val)
            return res