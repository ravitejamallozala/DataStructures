class Solution:
    def findRightInterval(self, intervals):
        int_hash = {}
        for ind, val in enumerate(intervals):
            int_hash[str(val)] = ind
        intervals.sort()
        ans = [-1] * len(intervals)
        for ind in range(len(intervals)):
            key_ind = int_hash.get(str(intervals[ind]))
            for ind_j in range(ind, len(intervals)):
                if intervals[ind][1] <= intervals[ind_j][0]:
                    ans[key_ind] = int_hash.get(str(intervals[ind_j]))
                    break
        return ans
        # ------------------------Better Solution------------------ runtime 300ms

    def findRightInterval_better(self, intervals):
        ind = dict()
        max_i = intervals[0][0]
        for i, rng in enumerate(intervals):
            ind[rng[0]] = i
            max_i = max(max_i, rng[0])

        out = [-1] * len(intervals)
        for i, rng in enumerate(intervals):
            last = rng[1]
            while last <= max_i and last not in ind:
                last += 1
            if last in ind:
                out[i] = ind[last]
        return out


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 4], [5, 7], [3, 4]]
    s.findRightInterval(intervals)

#
# def findRightInterval(self, intervals):
#     ints = sorted([[j, k, i] for i, [j, k] in enumerate(intervals)])
#     begs = [i for i, _, _ in ints]
#     out = [-1] * len(begs)
#     for i, j, k in ints:
#         t = bisect.bisect_left(begs, j)
#         if t < len(begs):
#             out[k] = ints[t][2]
#
#     return out
