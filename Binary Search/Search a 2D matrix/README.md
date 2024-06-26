

Notes:
TC: O(log m + log n)
SC: O(1)


1. Array approach will lead us to O(n^2)
2. Running Binary Search on matrix using top and bot to find the row, thus finding the row will have (log m) time complexity
3. Once the row is found, we run again the Binary Search on the selected row in step 2 and check if the value presents in the matrix. this will lead to (log n) time complexity.
4. Overall TC would be (log m + log n)
