# Power of Four
# Aug Week 1


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ans = n != 0 and ((n & (n - 1)) == 0) and not (n & 0xAAAAAAAA)
        print("ans", ans)
        return ans
