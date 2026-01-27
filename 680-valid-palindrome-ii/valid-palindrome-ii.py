class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left=0
        right= len(s)-1


        def isPalindrome(left,right):

            while left < right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        while left<right:

                if s[left]!= s[right]:
                    return isPalindrome(left, right-1) or isPalindrome(left+1, right)
                left+=1
                right-=1
        return True




        