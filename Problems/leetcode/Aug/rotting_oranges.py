"""
Rotten Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""


class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:

    def orangesRotting(self, grid):
        from collections import deque
        rotten = deque()
        fresh = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # print("Ele : ", grid[row][col])
                if grid[row][col] == 2:
                    rotten.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh.add((row, col))
        if not fresh:
            return 0
        ans = 0
        while rotten:
            rot = rotten.popleft()
            if (rot[0] + 1, rot[1]) in fresh:
                ans = rot[2] + 1 if ans < rot[2] + 1 else ans
                rotten.append((rot[0] + 1, rot[1], rot[2] + 1))
                fresh.remove((rot[0] + 1, rot[1]))
            if (rot[0], rot[1] + 1) in fresh:
                ans = rot[2] + 1 if ans < rot[2] + 1 else ans
                rotten.append((rot[0], rot[1] + 1, rot[2] + 1))
                fresh.remove((rot[0], rot[1] + 1))
            if (rot[0] - 1, rot[1]) in fresh:
                ans = rot[2] + 1 if ans < rot[2] + 1 else ans
                rotten.append((rot[0] - 1, rot[1], rot[2] + 1))
                fresh.remove((rot[0] - 1, rot[1]))
            if (rot[0], rot[1] - 1) in fresh:
                ans = rot[2] + 1 if ans < rot[2] + 1 else ans
                rotten.append((rot[0], rot[1] - 1, rot[2] + 1))
                fresh.remove((rot[0], rot[1] - 1))
        if fresh:
            return -1
        else:
            return ans


if __name__ == '__main__':
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    s = Solution()
    ans = s.orangesRotting(grid)
    print("Final ans:", ans)
    grid = [[0, 0], [0, 0], [1, 0], [1, 1], [2, 1], [0, 2], [1, 1]]
    s = Solution()
    ans = s.orangesRotting(grid)
    print("Final ans:", ans)
