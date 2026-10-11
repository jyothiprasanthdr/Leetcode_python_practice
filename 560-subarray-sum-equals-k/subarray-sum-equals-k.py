class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1} # base case where at index -1 imaginarily processed 0 elements and current sum is 0. 
       #so 0 occured once.  NeededPast SUm = CurrentSum - K 

        currsum =0
        cnt = 0
        for _ , num  in  enumerate(nums):

            currsum +=num
            neededPastSum= currsum-k
            if  neededPastSum in prefix:
                cnt+=prefix[neededPastSum]
            prefix[currsum]=prefix.get(currsum, 0)+1
        return cnt
