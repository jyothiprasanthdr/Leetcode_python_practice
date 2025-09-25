class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for ind, num in enumerate(nums):

            if num in map:
                return [ind, map[num]]
            
            else :
                map[target-num]= ind
        
        