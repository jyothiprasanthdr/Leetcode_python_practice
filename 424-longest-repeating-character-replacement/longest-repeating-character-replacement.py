class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0
        count = [0]*26
        maxCount= 0
        best=0
        for r, c in enumerate(s):

            idx = ord(c)-ord('A')
            count[idx]+=1
            maxCount = max(maxCount, count[idx])

            while (r-l+1)-maxCount > k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            best = max(best, r-l+1)
        return best