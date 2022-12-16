class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0

        for i in range(1,len(prices)):
            profit = prices[i] - min_price
            max_price = max(max_price , profit)
            min_price = min(min_price , prices[i])

        return max_price