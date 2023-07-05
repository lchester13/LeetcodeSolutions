# Greedy Algorithms

class LeetCodeSolutions:
    #121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices):
        """
        get the max profit 
        """
        left, right = 0, 1 # left is buy, right is sell
        maxProf = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProf = max(profit, maxProf)
            else:
                left = right
            right+= 1
        return maxProf