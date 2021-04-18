prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices:
            if i < buy: buy = i
            elif i - buy > profit: profit = i - buy
        return profit