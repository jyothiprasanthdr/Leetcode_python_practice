class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map = {}

        for i, ch in enumerate(s):
            if ch in map:
                if map[ch] != t[i]:
                    return False
            else:
                if t[i] not in map.values():
                    map[ch] = t[i]
                else:
                    return False

        return True
