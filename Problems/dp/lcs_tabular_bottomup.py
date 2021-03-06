"""
LeetCode
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.


Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

Solution:
Bottom Up Approach -> Tabulation
"""


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        #  As Base Conditon:
        # if m==0 or n==0 O/P: 0
        # So, Intialising first row and column with 0
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        # print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[m - 1] == text2[n - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    text1 = "abc"
    text2 = "abc"
    ans = s.longestCommonSubsequence(text1, text2)
    print(ans)
