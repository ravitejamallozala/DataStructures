'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
'''


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        d = {}
        for i in range(n):
            if i == 0:
                print(i, "ele", A[i])
                d[A[i]] = 0
                continue
            if A[i] in d:
                print("element is", A[i])
                return A[i]
            else:
                print("entered one", True)
                d[A[i]] = 0


test1 = [1, 2, 3, 3]
sol = Solution()
print(sol.repeatedNTimes(test1))
