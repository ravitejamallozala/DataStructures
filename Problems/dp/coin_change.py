"""
LeetCode: 322. Coin Change (Least number of coins )
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


# Intialise


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        l = len(coins)
        if not l:
            return -1
        dp = [[0 for _ in range(amount + 1)] for __ in range(l + 1)]
        for i in range(amount + 1):
            dp[0][i] = amount + 1
        print(dp)
        print(l)
        for i in range(1, l + 1):
            for j in range(1, amount + 1):
                print(i, j)
                if coins[i - 1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[l][amount]


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amt = 11
    print(s.coinChange(coins, amt))
