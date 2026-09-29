class NumArray:

    def __init__(self, nums: list[int]):
        self.sums = [0]
        for n in nums:
            self.sums.append(self.sums[-1]+n)
       
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)