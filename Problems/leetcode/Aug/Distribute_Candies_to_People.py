"""
Distribute Candies to People

Solution
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.



Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000

Hint = Arthimetic progression Formulas
Sum of arthimetic progression
and An = a + (n-1)d
Sn = (n/2) (2a + (n-1)d)
Sn = (4/2) (2*1 + (4-1)1)
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        import math
        ans = [0] * num_people
        turns = int((-1 + math.sqrt(1 + 8 * candies)) // (2 * num_people))
        remaining = candies - ((turns * num_people) * (turns * num_people) + (turns * num_people)) // 2
        for ind in range(num_people):
            old_val = ((2 * (ind + 1)) + (turns - 1) * num_people) * turns
            ans[ind] = int(old_val // 2)
            print(ans)
            if not remaining > 0:
                continue
            curr_val = (ind + 1) + turns * num_people
            print(curr_val)
            if remaining - curr_val > 0:
                remaining = remaining - curr_val
                ans[ind] += curr_val
            else:
                ans[ind] += remaining
                remaining = 0
        return ans


# [27,18,21,24]

if __name__ == '__main__':
    s = Solution()
    candies = 90
    ppl = 4
    ans = s.distributeCandies(candies, ppl)
    print(ans)
