class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []

        res = []

        window_count = [0]*26
        p_count = [0]*26
        a= ord('a')
        for i in range(len(p)):
            p_count[ ord(p[i]) - a ]+=1
            window_count[ord(s[i])-a]+=1

        if p_count== window_count:
            res.append(0)
        for i in range(len(p), len(s)):

            window_count[ ord(s[i- len(p)])-a]-=1
            window_count[ord(s[i])-a ]+=1
            if window_count == p_count:
                res.append(i - len(p)+1)
        return res