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
Bottom up
"""


class Solution:

    def findLength(self, A, B) -> int:
        m = len(A)
        n = len(B)
        self.max = 0
        #  As Base Conditon:
        # if m==0 or n==0 O/P: 0
        # So, Intialising first row and column with 0
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        # print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    self.max = max(self.max, dp[i][j])
                # else:
                #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return self.max


if __name__ == '__main__':
    s = Solution()
    A= [1, 2, 3, 2, 1]
    B= [3, 2, 1, 4, 7]
    ans = s.findLength(A, B)
    print(ans)
