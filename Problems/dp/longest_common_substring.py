"""
718. Maximum Length of Repeated Subarray
Medium

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

Solution:
Recursion + Memorisation
"""


class Solution:
    def lcs(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0
        if self.dp[m][n] != -1:
            self.max = max(self.max, self.dp[m][n])
            return self.dp[m][n]
        
        if s1[m - 1] == s2[n - 1]:
            self.dp[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1)
            self.max = max(self.max, self.dp[m][n])
        # self.max = max(self.max, self.dp[m][n])
        return self.dp[m][n]

    def findLength(self, A, B) -> int:
        m = len(A)
        n = len(B)
        self.max = 0
        self.dp = [[-1 for _ in range(n + 1)] for __ in range(m + 1)]

        self.lcs(A, B, m, n)
        print(self.dp)
        return self.max


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    ans = s.findLength(A, B)
    print(ans)
