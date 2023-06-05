class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float('inf')
        for i in range(0,len(prices)):
            minprice = min(minprice,prices[i])
            maxprofit = max(maxprofit,prices[i]-minprice)
        return maxprofit
