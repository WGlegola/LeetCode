class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP = float('inf')
        maxP = 0
        for i in range(len(prices)):
            if prices[i]<minP:
                minP = prices[i]
            elif prices[i]-minP>profit:
                profit=prices[i]-minP
        return profit
            
            
        