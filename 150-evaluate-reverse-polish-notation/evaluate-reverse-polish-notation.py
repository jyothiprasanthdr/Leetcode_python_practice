class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []


        for i in tokens:
            
            if i in ['+','*','/','-']:
                if stack:
                    p1=int(stack.pop())
                    p2= int(stack.pop())
                if i=='+':
                    stack.append(p1+p2)
                elif i=='-':
                    stack.append(p2-p1)
                elif i=='*':
                    stack.append(p1*p2)
                else:
                    stack.append(p2/p1)
            else:
                stack.append(i)
        return int(stack[-1])


        