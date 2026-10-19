class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)

        for i, val in enumerate(temperatures):

            while stack and stack[-1][0] < val:
                
                prev_temp, prev_ind = stack.pop()
                res[prev_ind]= i - prev_ind
            stack.append([val, i])
        return res