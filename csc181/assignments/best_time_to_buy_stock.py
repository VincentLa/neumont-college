class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        buy = 0 
        buy_price = 0
        profit = 0
        idx = 0 
        while idx < len(prices) - 1:
            if prices[idx + 1] > prices[idx] and buy == 0:
                buy = 1
                buy_price = prices[idx]
            if prices[idx] > buy_price and buy == 1:
                buy = 0
                profit += prices[idx] - buy_price
            if prices[idx + 1] > prices[idx] and buy == 0:
                buy = 1
                buy_price = prices[idx]
            idx += 1
        if prices[idx] > buy_price and buy == 1:
            buy = 0
            profit += prices[idx] - buy_price
        return profit