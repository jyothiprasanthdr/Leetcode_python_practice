class MinStack:
    


    def __init__(self):
        self.stack = []
        self.minvalue=[]
        # self.minvalue[0]=float('inf')

        
    def push(self, value: int) -> None:
        self.stack.append(value)
        value = min(value, self.minvalue[-1] if self.minvalue else value)
        self.minvalue.append(value)
        

    def pop(self) -> None:
       self.stack.pop()
       self.minvalue.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minvalue[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()