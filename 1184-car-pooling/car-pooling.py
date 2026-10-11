class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:

        ans = [0]* 1001


        for passengers, from_, to_ in trips:

            ans[from_] += passengers
            ans[to_]-= passengers

        curr_passengers =0

        for i in ans:

                curr_passengers +=i

                if curr_passengers > capacity:
                    return False
        return True