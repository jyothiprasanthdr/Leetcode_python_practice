class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      
        count =0
        found=False

        for ch in reversed(s):
            
            if ch.isalpha():
                count+=1
                found=True
            elif found:
                return count
        
        return count


            