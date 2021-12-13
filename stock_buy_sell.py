class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_cost = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if max_cost < prices[i] - min_price:
                max_cost = prices[i] - min_price
        return max_cost