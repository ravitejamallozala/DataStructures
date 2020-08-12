class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations)-1, -1 , -1):
            # print("num", citations[i], "ind", i+1)
            if citations[i] >= i + 1:
                return i+1
            print(i)

# driver code
if __name__ == '__main__':
    s = Solution()
    a = [3,0,6,1,5]
    print("finale ", s.hIndex(a))
