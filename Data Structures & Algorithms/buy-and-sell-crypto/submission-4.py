class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        for i in range(len(prices) - 1):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
            

        return max_profit