class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left =0
        window = defaultdict(int)

        for right in range(len(s)):

            window[s[right]]+=1

    
            while window[s[right]]>1:

                window[s[left]]-=1
                left+=1
            max_len= max(max_len, right-left+1)
        
        return max_len