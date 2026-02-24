class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1

            while l<r:

                current_sum = nums[i]+ nums[l]+ nums[r]

                if abs(current_sum-target) < abs(closest-target):
                    closest= current_sum

                if current_sum ==target:
                    return current_sum
                elif current_sum < target:
                    l+=1
                else:
                    r-=1
        return closest