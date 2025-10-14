class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        k = len(needle)
        l=0
        window = haystack[l:k]
        if window == needle:
            return 0
        res =-1
        for r in range(k, len(haystack)):

            window = haystack[l+1:r+1]
            if window == needle:
                return l+1
            l+=1
           
        return -1


           
           


        