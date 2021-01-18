# class Solution:
#     def is_palindrome(self, s, i, j):
#         if i >= j:
#             return True
#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
#
#     def partition(self, s, i, j):
#         if i >= j:
#             return 0
#         if self.dp[i][j] != -1:
#             return self.dp[i][j]
#         if self.is_palindrome(s, i, j):
#             return 0
#         ans = self.len
#         for k in range(i, j):
#             temp = 1 + self.partition(s, i, k) + self.partition(s, k + 1, j)
#             ans = min(temp, ans)
#         self.dp[i][j] = ans
#         return ans
#
#     def minCut(self, s: str) -> int:
#         self.len = len(s)
#         self.dp = [[-1 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
#         ans = self.partition(s, 0, len(s) - 1)
#
#         return ans


# Version: Optimization
# class Solution:
#     def is_palindrome(self, t):
#         return t == t[::-1]
#
#     def partition(self, s, i, j):
#         if i >= j:
#             return 0
#         if self.dp[i][j] != -1:
#             return self.dp[i][j]
#         if self.is_palindrome(s[i:j+1]):
#             return 0
#         ans = self.len
#         for k in range(i, j):
#             if self.dp[i][k] != -1:
#                 left = self.dp[i][k]
#             else:
#                 left = self.partition(s, i, k)
#                 self.dp[i][k] = left
#             if self.dp[k + 1][j] != -1:
#                 right = self.dp[k + 1][j]
#             else:
#                 right = self.partition(s, k + 1, j)
#                 self.dp[k + 1][j] = right
#             temp = 1 + right + left
#             ans = min(temp, ans)
#         self.dp[i][j] = ans
#         return ans
#
#     def minCut(self, s: str) -> int:
#         self.len = len(s)
#         self.dp = [[-1 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
#         ans = self.partition(s, 0, len(s) - 1)
#
#         return ans
class Solution:
    def is_palindrome(self, t):
        return t == t[::-1]

    def partition(self, s, i, j):
        if i >= j:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        elif self.p_cache.get((i, j)):
            return 0  # since,
        elif self.is_palindrome(s[i:j+1]):
            self.p_cache[(i, j)] = True
            return 0
        ans = self.len
        for k in range(i, j):
            if self.is_palindrome(s[i: k+1]):
                left = 0
                right = self.partition(s, k + 1, j)
                self.dp[k + 1][j] = right
                temp = 1 + right + left
                ans = min(temp, ans)
                self.dp[i][j] = ans
        return ans

    def minCut(self, s: str) -> int:
        self.len = len(s)
        self.p_cache= {}
        self.dp = [[-1 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        ans = self.partition(s, 0, len(s) - 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    inp = "nitin"
    ans = s.minCut(inp)
    print(ans)
