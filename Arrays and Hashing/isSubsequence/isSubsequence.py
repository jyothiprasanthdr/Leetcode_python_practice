class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for c in t:
            if s and c == s[0]:
                s.pop(0)
        return len(s) == 0
