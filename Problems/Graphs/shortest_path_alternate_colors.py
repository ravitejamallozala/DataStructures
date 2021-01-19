# 1129. Shortest Path with Alternating Colors
# Graphs

# Add color in Visited Node to check


class Solution:
    red_hash = {}
    blue_hash = {}

    def __init__(self):
        self.red_hash = {}
        self.blue_hash = {}

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        for i in red_edges:
            if i[0] in self.red_hash:
                self.red_hash.get(i[0]).append(i[1])
            else:
                self.red_hash[i[0]] = [i[1]]
        for i in blue_edges:
            if i[0] in self.blue_hash:
                self.blue_hash.get(i[0]).append(i[1])
            else:
                self.blue_hash[i[0]] = [i[1]]
        print("red_hash:", self.red_hash)
        print("blue hash:", self.blue_hash)
        answer = []
        for x in range(n):
            red = self.shortest_path(x, 0, None, {}, "R")
            blue = self.shortest_path(x, 0, None, {}, "B")
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

    def shortest_path(self, x, curr, from_node, visited, in_hash):
        if x == curr:
            return 0
        if curr in visited:
            if str(from_node) + in_hash in visited[curr]:
                return
            else:
                visited[curr].append(str(from_node) + in_hash)
        else:
            visited[curr] = [str(from_node) + in_hash]
        if in_hash == "R":
            if curr in self.red_hash:
                vals = self.red_hash.get(curr)
                ans = []
                for val in vals:
                    res = self.shortest_path(x, val, curr, visited, "B")
                    if res is not None:
                        ans.append(1 + res)
                return min(ans) if ans else None

        elif in_hash == "B":
            if curr in self.blue_hash:
                vals = self.blue_hash.get(curr)
                ans = []
                for val in vals:
                    res = self.shortest_path(x, val, curr, visited, "R")
                    if res is not None:
                        ans.append(1 + res)
                return min(ans) if ans else None


# Driver code
if __name__ == '__main__':
    # n = 3
    # red_edges = [[0, 1], [0, 2]]
    # blue_edges = [[1, 0]]
    # n = 5
    # red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    #
    # blue_edges =[[1, 2], [2, 3], [3, 1]]
    # n = 5
    # red_edges = [[1, 4], [0, 3]]
    # blue_edges = [[3, 1], [3, 4]]

    # n = 5
    # red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    #
    # blue_edges = [[1, 2], [2, 3], [3, 1]]
    n = 5
    red_edges = [[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4], [3, 4]]
    blue_edges = [[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]
    s = Solution()
    s.shortestAlternatingPaths(n, red_edges, blue_edges)