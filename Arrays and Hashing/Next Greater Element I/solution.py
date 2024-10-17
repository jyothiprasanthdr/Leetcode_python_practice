class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        nums1_map = {n: i for i, n in enumerate(nums1)}
        for i in nums2:

            while stack and stack[-1] < i:
                val = stack.pop()
                ind = nums1_map[val]
                res[ind] = i

            if i in nums1:
                stack.append(i)
        return res
