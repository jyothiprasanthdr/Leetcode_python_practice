class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.strip().split(" ")
        return len(t[-1])

        