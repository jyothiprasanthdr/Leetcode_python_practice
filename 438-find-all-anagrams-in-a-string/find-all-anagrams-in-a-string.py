class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []

        check = [0]*26
        window = [0]*26
        offset = ord('a')
        for i in range(len(p)):
            check[ord(p[i])- offset]+=1
            window[ord(s[i]) - offset]+=1
        res = []
        if check ==window:
            res.append(0)

        for i in range(len(p), len(s)):

           window[ ord(s[i - len(p)]) -offset] -=1
           window[ord(s[i])-offset]+=1
           if window == check:
            res.append(i - len(p)+1)

        return res


