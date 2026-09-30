class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0]*(cols+1) for r in range(rows+1)]


        for r in range(rows):
            for c in range(cols):

                current= matrix[r][c]
                top= self.prefix[r][c+1]
                left= self.prefix[r+1][c]
                topleft= self.prefix[r][c]
                self.prefix[r+1][c+1] = current + top +left-topleft
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        r1,c1,r2,c2 = row1+1, col1+1, row2+1, col2+1

        bottomright = self.prefix[r2][c2]
        top = self.prefix[r1-1][c2]
        left = self.prefix[r2][c1-1]
        topleft= self.prefix[r1-1][c1-1]

        return (bottomright-top-left+topleft)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)