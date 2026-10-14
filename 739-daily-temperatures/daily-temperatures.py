class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
           
            while stack and temp > stack[-1][0]:
             
                stack_val, stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind

            stack.append([temp,i])
        return res