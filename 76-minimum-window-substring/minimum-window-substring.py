class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
             return ""

        window_counter, t_counter = {},{}
        

        for c in t:
            t_counter[c] = 1 + t_counter.get(c,0)

        have, need = 0 , len(t_counter)
        l=0
        res, resLen = [-1,-1], float('inf')
        for r in range(len(s)):
            c=s[r]
            window_counter[c] = 1 + window_counter.get(c,0)

            if c in t_counter and window_counter[c]==t_counter[c]:

                have+=1
                
                while have == need:

                    if (r-l+1) < resLen:

                        res=[l,r]
                        resLen = (r-l+1)
                    window_counter[s[l]]-=1
                    if s[l] in t_counter and window_counter[s[l]] < t_counter[s[l]]:
                        have-=1
                    l+=1
        l,r = res

        return s[l:r+1]
                

                    




        