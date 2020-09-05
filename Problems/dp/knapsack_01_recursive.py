"""
Topic: DP
Problem Link: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
"""
# Recursive Code will not work Because of  Time limit exceeded error
class Knapsack:
    def max_profit(self, wts, vals, n, w):
        # Base Cond
        if n == 0 or w == 0:
            return 0
        # Choice Diagram
        if wts[n - 1] <= w:  # then only we have choice of including or excluding
            return max(self.max_profit(wts, vals, n - 1, w), vals[n - 1] + self.max_profit(wts, vals, n - 1,
                                                                                           w - wts[n - 1]))
        else:
            return self.max_profit(wts, vals, n - 1, w)

    def driver_code(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            w = int(input())  # Capacity
            vals = list(map(int, input().split(' ')[:n]))
            wts = list(map(int, input().split(' ')[:n]))
            ans = self.max_profit(wts, vals, n, w)
            print(ans)


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
