"""
Random Point in Non-overlapping Rectangles
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates.
A point on the perimeter of a rectangle is included in the space covered by the rectangles.
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]
Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.


"""


class Solution(object):

    def __init__(self, rects):
        self.s = []
        cumul = 0
        for r in rects:
            x, y = r[2] - r[0] + 1, r[3] - r[1] + 1
            cumul += x * y
            self.s.append(cumul)
        self.rects = rects

    def pick(self):
        import random
        r = random.randint(0, self.s[-1])
        lo, hi = 0, len(self.s) - 1
        while (lo < hi):
            med = (lo + hi) >> 1
            if self.s[med] > r:
                hi = med
            else:
                lo = med + 1

        x = self.rects[lo][0] + random.randint(0, self.rects[lo][2] - self.rects[lo][0])
        y = self.rects[lo][1] + random.randint(0, self.rects[lo][3] - self.rects[lo][1])
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
if __name__ == '__main__':
    fun = ["Solution", "pick", "pick", "pick"]
    vals = [[[[1, 1, 5, 5]]], [], [], []]
