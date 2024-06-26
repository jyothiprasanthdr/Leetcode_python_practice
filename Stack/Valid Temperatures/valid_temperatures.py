class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for ind, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                stack_val, stack_ind = stack.pop()
                res[stack_ind] = ind - stack_ind
            stack.append([val, ind])
        return res
