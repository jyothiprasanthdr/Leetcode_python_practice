class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window = sum(nums[:k])
        ans = window
        for r in range(k, len(nums)):

            l = r - k
            window -= nums[l]
            window += nums[r]
            ans = max(ans, window)
        return ans/k