"""
Best Time to Buy and Sell Stock III

Solution
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Ans explaination: https://www.youtube.com/watch?v=0FKn0FSIQYE
"""
class Solution:
    def maxProfit(self, prices) -> int:
        l = len(prices)
        if l < 1:
            return 0

        min_price = prices[0]
        profit_left = [0] * l
        max_profit = 0
        for ind in range(l):
            min_price = prices[ind] if prices[ind] < min_price else min_price
            profit_left[ind] = prices[ind] - min_price if prices[ind] - min_price > max_profit else max_profit
            max_profit = profit_left[ind]
        max_price = prices[l - 1]
        profit_rit = [0] * l
        max_profit = 0
        for ind in range(l - 1, 0, -1):
            profit_rit[ind] = max_price - prices[ind] if max_price - prices[ind] > max_profit else max_profit
            max_profit = profit_rit[ind]
            max_price = prices[ind] if prices[ind] > max_price else max_price
        max_sum = 0
        for i in range(l):
            max_sum = profit_rit[i] + profit_left[i] if profit_rit[i] + profit_left[i] > max_sum else max_sum
        return max_sum


if __name__ == "__main__":
    s = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [1, 2, 3, 4, 5]
    # prices = [7, 6, 4, 3, 1]
    ans = s.maxProfit(prices)
    print("Final Ans:", ans)
