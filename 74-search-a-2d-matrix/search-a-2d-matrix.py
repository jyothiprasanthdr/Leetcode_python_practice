class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l=0
        row= len(matrix)
        col= len(matrix[0])
        r= row*col-1

        while l<=r:

            mid = (l+r)//2
            m= matrix[mid//col][mid%col]

            if m==target:
                return True
            elif m>target:
                r=mid-1
            else:
                l=mid+1
        return False
