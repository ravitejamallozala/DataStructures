"""
Leet
518. Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1"""


class Solution:
    def change(self, amount: int, coins) -> int:
        l = len(coins)
        if not l:
            return 0

        dp = [[0 for _ in range(amount + 1)] for __ in range(l + 1)]
        for i in range(l + 1):
            dp[i][0] = 1

        print(dp)
        print(l)
        for i in range(1, l + 1):
            for j in range(1, amount + 1):
                print(i, j)
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[l][amount]


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amt = 5
    print(s.change(amt, coins))
