""""
Print Spiral matrix
1   2  3   4
5   6   7  8
9  10 11 12
13 14 15 16


1
2
3
4
8
12
16
15
14
13
9
5
6
7
11
10
"""



class PrintArray:
    def __init__(self, arr):
        self.arr = arr
        self.rsize = len(arr)
        self.csize = len(arr[0])

    def print_spiral_matrix(self, arr, x, y, depth, direction):
        count = 0
        for i in range(depth):
            # Check x & y
            print(arr[x][y])
            count +=1
            if direction == 'r':
                y += 1
                if y == self.csize:
                    self.print_spiral_matrix(arr, x+1, y-1, depth-1, 'd')
                    break
            elif direction == 'l':
                y -= 1
                if y < 0:
                    self.print_spiral_matrix(arr, x-1, y+1, depth-1, 'u')
                    break

            elif direction == 'd':
                x += 1
                if x == self.rsize:
                    self.print_spiral_matrix(arr, x-1, y-1, depth, 'l')
                    break

            elif direction == 'u':
                x -= 1
                if count == depth:
                    self.print_spiral_matrix(arr, x+1, y+1, depth, 'r')
                    break



arr = [[1, 2, 3, 4, 41], [5, 6, 7, 8, 81], [9, 10, 11, 12, 141], [13, 14, 15, 16, 161]]
p = PrintArray(arr)
p.print_spiral_matrix(arr, 0, 0, len(arr[0]), 'r')


# changes -> COnsider mxn Mattrix