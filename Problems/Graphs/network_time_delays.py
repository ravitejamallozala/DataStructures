class Solution:
    def check_all_visited(self, arr):
        for i in arr:
            if i is 0:
                return False
        return True

    def networkDelayTime(self, times, n: int, k: int) -> int:
        from collections import defaultdict, deque
        if not times: return -1

        time_dict = {}
        edge_dict = defaultdict(list)
        # Intialising edge and time dicts
        for fr, to, time in times:
            time_dict[(fr, to)] = time
            edge_dict[fr].append(to)
        time_dict[(0, k)] = 0
        visited = [0 for i in range(n)]
        time_added = [0 for i in range(n)]
        print("egde dict", edge_dict)
        print("time_dict", time_dict)
        total_time = 0
        q = deque()
        q.append((0, k))
        while (q):
            root, ele = q.popleft()
            # if not visited[ele - 1] is 0:
            #     continue
            visited[ele - 1] = 1
            print("processed ", root, ele)
            # if root > 0 and time_added[root - 1] is 0:
            #     time_added[root - 1] = 1
            #     total_time += time_dict[(root, ele)]
            #     print( "adding time " , root , "->", ele, total_time)
            if ele not in edge_dict:
                print("edge not found from source")
                continue
            else:
                max = float('-inf')
                for i in edge_dict[ele]:
                    if max < time_dict[ele,i] and visited[i-1] == 0 :
                        max = time_dict[ele,i]
                        visited[i - 1] = 1
                    q.append((ele, i))
                total_time += max
            if self.check_all_visited(visited):
                return total_time
        if self.check_all_visited(visited):
            return total_time
        else:
            return -1
s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
# times = [[1,2,1],[2,1,3]]
# times = [[1,2,1],[2,3,2],[1,3,2]]

ans= s.networkDelayTime(times, 4, 2)
print(ans)