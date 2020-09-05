"""
Topic: DP
Problem Link: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
"""


# Recursive Code With Memorization
class Knapsack:
    def max_profit(self, wts, vals, n, w):
        # Base Cond

        if n == 0 or w <= 0:
            return 0

        # Choice Diagram
        if self.dp[n][w] != -1:
            return self.dp[n][w]
        if wts[n - 1] <= w:  # then only we have choice of including or excluding
            self.dp[n][w] = max(self.max_profit(wts, vals, n - 1, w - wts[n - 1]) + vals[n - 1],
                                self.max_profit(wts, vals, n - 1, w))
        else:
            self.dp[n][w] = self.max_profit(wts, vals, n - 1, w)
        return self.dp[n][w]

    def driver_code(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            w = int(input())  # Capacity
            vals = list(map(int, input().split(' ')[:n]))
            wts = list(map(int, input().split(' ')[:n]))
            self.dp = [[-1] * (w + 1)] * (n + 1)
            self.max_profit(wts, vals, n, w)
            print(self.dp[n][w])


if __name__ == '__main__':
    s = Knapsack()
    s.driver_code()

# 2
# 3
# 4
# 1 2 3
# 4 5 1
# 3
# 3
# 1 2 3
# 4 5 6
