class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        window = set()
        l=0
        ans = float('inf')
        for r in range(len(cards)):

            while cards[r] in window:

                ans = min(ans, r-l+1)
                window.remove(cards[l])
                l+=1
            window.add(cards[r])
        return ans if ans !=float('inf') else -1