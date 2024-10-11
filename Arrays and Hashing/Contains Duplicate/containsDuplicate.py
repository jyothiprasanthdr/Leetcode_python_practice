class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_hp = {}

        for elem in nums:
            if elem not in nums_hp:
                nums_hp[elem] = 1
            else:
                return True

        return False
