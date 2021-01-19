"""
667. Beautiful Arrangement II
https://leetcode.com/problems/beautiful-arrangement-ii/
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        num = 1
        num_set = {i for i in range(2, n + 1)}
        print(num_set)
        arr = []
        dist_num = True
        for _ in range(n):
            # print("\nbefore ","k ", k , "num: ", num, "arr: ", arr, num_set)

            arr.append(num)
            if dist_num == True:
                if num - k in num_set:
                    num = num - k
                    num_set.remove(num)
                elif num + k in num_set:
                    num = num + k
                    num_set.remove(num)
            elif dist_num == False and num_set:
                num = num_set.pop()

            # print("after","k ", k , "num: ", num, "arr: ", arr)
            k -= 1
            if k == 0:
                dist_num = False
        return arr