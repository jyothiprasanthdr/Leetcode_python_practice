
![alt text](<Screenshot 2024-06-25 at 10.39.04 PM.png>)



TC: O(n)
SC:O(n)


Notes:

1. Array Approach requires O(n^2)
2. Use a Stack approach, by maintaining monotonically decreasing stack
3. Whenever the current temperature is greater than top element in stack, pop the element and update the result list with that index.


