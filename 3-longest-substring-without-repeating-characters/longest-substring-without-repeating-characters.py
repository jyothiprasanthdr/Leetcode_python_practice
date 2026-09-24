class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        counter=defaultdict(int)


        for right in range(len(s)):
             counter[s[right]]+=1


             while counter[s[right]]>1:
                
                counter[s[left]]-=1
                left+=1
             max_len= max(max_len, right-left+1)
        return max_len


        