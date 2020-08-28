"""
  Implement Rand10() Using Rand7()
Link: https://leetcode.com/problems/implement-rand10-using-rand7/
Solution
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().



Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.


Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?

"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def __init__(self):
        self.count_arr = [0] * 7
        self.call_count = 0
        self.number = 8

    def rand10(self):
        """
        :rtype: int
        """
        self.call_count += 1
        if self.call_count == 10:
            self.call_count = 0
            self.count_arr = [0] * 7
            self.number = 8
        num = rand7()
        # print("->", num)
        if self.count_arr[num - 1] == 1 and self.number != 11:
            ans = self.number
            self.number += 1
            # print("ans1", ans, "number", self.number)
            return ans
        elif self.count_arr[num - 1] == 1 and self.number == 11:
            while (self.count_arr[num - 1] == 1):
                # print("inside, ",num)
                num = rand7()
            self.count_arr[num - 1] = 1

            # print("ans_inside", num, "number", self.number)
            return num
        else:
            ans = num
            self.count_arr[num - 1] = 1

            # print("ans3", ans, "number", self.number)
            return ans


