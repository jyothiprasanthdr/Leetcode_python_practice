class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [ [0]* (cols+1) for r in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                top = self.prefix[r][c+1]
                left= self.prefix[r+1][c]
                topleft =self.prefix[r][c]
                self.prefix[r+1][c+1]= matrix[r][c]+left+top-topleft 
        print(self.prefix)           

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2= row1+1, row2+1
        c1,c2 = col1+1, col2+1

        return self.prefix[r2][c2] + self.prefix[r1-1][c1-1] - self.prefix[r1-1][c2]- self.prefix[r2][c1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)