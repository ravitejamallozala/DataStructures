class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for char in s:
            ans = ans * 26
            ans += ord(char) - 64
        return ans


# Driver Code
if __name__ == '__main__':
    s = Solution()
    ans = s.titleToNumber("AAA")
    print("Final ANs:", ans)
