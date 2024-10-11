class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = len(arr) - 1
        max_seen = -1
        while r >= 0:
            tmp = arr[r]
            arr[r] = max_seen
            max_seen = max(max_seen, tmp)
            r -= 1
        return arr
