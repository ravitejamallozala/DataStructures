class Solution:
    def __init__(self):
        self.next_max = None


    def rev_arr(self, k, key):
        i = 0
        while i <= k:
            self.next_max = i if key == self.arr[k] else self.next_max
            self.next_max = k if key == self.arr[i] else self.next_max
            self.arr[i], self.arr[k] = self.arr[k], self.arr[i]
            i += 1
            k -= 1
        print("reversed", self.arr, self.next_max)

    def pancakeSort(self, A):
        max_val = len(A)
        max_ind = None
        self.arr = A
        for i in range(len(A)):
            if max_val == A[i]:
                max_ind = i
                break
        ans = []
        for _ in range(len(A)-1):
            self.rev_arr(max_ind, max_val - 1)
            self.rev_arr(max_val - 1, max_val - 1)
            ans.extend([max_ind+1, max_val])
            max_val -= 1

            max_ind = self.next_max
        print("Final ", self.arr)
        print(ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    inp = [3, 2, 4, 1]
    # inp = [5, 4, 3, 2, 1]
    s.pancakeSort(inp)
