"""
Non-overlapping Intervals

Solution
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
"""
3 types of Cases:
[1,3],[1,10]
[1,5] & [6,10] - No overlaps => dont remove anything
[1,5] & [2,3] - Internal overlap => remove the bigger range one
[2,5] & [3,6] - Partial overlap => remove the right extra one (we are sorting so removing right will prevent more overlaps)
"""


class Solution:

    def __init__(self):
        self.count = 0
        self.prev = None

    def check_overlap(self, a, b):
        if a[1] <= b[0]:
            self.prev = b
        elif a[0] <= b[0] and a[1] >= b[1]:
            self.prev = b
            self.count += 1
        elif a[0] <= b[0] and b[1] > a[1]:
            self.prev = a
            self.count += 1
        elif a[0] <= b[0] and a[1] > b[1]:
            self.count += 1
            return

    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: [x[0], x[1]])
        self.prev = intervals[0]
        print(intervals)
        for i in range(1, len(intervals), 1):
            self.check_overlap(self.prev, intervals[i])
        return self.count


if __name__ == '__main__':
    s = Solution()
    inter = [[1, 3], [1, 2], [2, 3], [3, 4]]
    # inter = [[1, 2], [1, 2], [1, 2]]
    # inter = [[1, 2], [2, 3]]
    ans = s.eraseOverlapIntervals(inter)
    print(ans)
