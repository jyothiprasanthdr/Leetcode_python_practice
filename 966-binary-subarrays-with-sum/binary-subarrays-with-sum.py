class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(k: int)->int:
            if k <0:
                return 0
            currsum=0
            l=0
            total_subarrays=0
            for r in range(len(nums)):

                currsum += nums[r]

                while currsum > k:

                    currsum-=nums[l]
                    l+=1
                total_subarrays += (r-l+1)
            return total_subarrays

        return atmost(goal)- atmost(goal-1)