# 1129. Shortest Path with Alternating Colors
# Graphs


class Solution:
    red_hash = {}
    blue_hash = {}

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        for i in red_edges:
            if i[0] in self.red_hash:
                arr = self.red_hash.get(i[0])
                arr.append(i[1])
                self.red_hash[i[0]] = arr
            else:
                self.red_hash[i[0]] = [i[1]]
        for i in blue_edges:
            if i[0] in self.blue_hash:
                arr = self.blue_hash.get([i[0]])
                arr.append(i[1])
                self.blue_hash[i[0]] = arr
            else:
                self.blue_hash[i[0]] = [i[1]]
        print("red_hash:", self.red_hash)
        print("blue hash:", self.blue_hash)
        answer = []
        for x in range(n):
            red = self.shortest_path(x, 0, [False] * n, "R")
            blue = self.shortest_path(x, 0, [False] * n, "B")
            if red is not None and blue is not None:
                answer.append(min(red, blue))
            elif red is not None:
                answer.append(red)
            elif blue is not None:
                answer.append(blue)
            else:
                answer.append(-1)
            print("main ans ", x, ": ", answer[x])
        return answer

    def shortest_path(self, x, curr, visited, in_hash):
        if x == curr:
            return 0
        if visited[curr] is True:
            return
        visited[curr] = True
        if in_hash == "R":
            if curr in self.red_hash:
                vals = self.red_hash.get(curr)
                ans = []
                for val in vals:
                    res = self.shortest_path(x, val, visited, "B")
                    if res is not None:
                        ans.append(1 + res)
                return min(ans) if ans else None

        elif in_hash == "B":
            if curr in self.blue_hash:
                vals = self.blue_hash.get(curr)
                ans = []
                for val in vals:
                    res = self.shortest_path(x, val, visited, "R")
                    if res is not None:
                        ans.append(1 + res)
                return min(ans) if ans else None
            # else:
            #     return -1000


# Driver code
if __name__ == '__main__':
    # n = 3
    # red_edges = [[0, 1], [1, 2]]
    # blue_edges = []
    n = 5
    red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

    blue_edges =[[1, 2], [2, 3], [3, 1]]
    s = Solution()
    s.shortestAlternatingPaths(n, red_edges, blue_edges)
