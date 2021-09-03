import sys
from queue import PriorityQueue

# def find_cost(arr):
#     size = len(arr)
#     result_value = 0
#     initial_value = 0
#     min_heap = PriorityQueue()
#
#     for ind in range(size):
#         prev = 0
#         if not min_heap.empty():
#             prev = min_heap.get()
#             min_heap.put(prev)
#         if not min_heap.empty() and prev < arr[ind]:
#             initial_value = arr[ind] - prev
#             result_value += initial_value
#             min_heap.get()
#         min_heap.put(arr[ind])
#     return result_value
#
#
# def modifyArray(arr):
#     min_val = min(find_cost(arr), find_cost(arr[::-1]))
#     return min_val

data_Arr = [[0 for i in range(1000)]
            for j in range(1000)]


def find_cost(data_Arr, arr, size, min_Val, max_val):
    if (size == 0):
        return 0
    if (data_Arr[size][max_val]):
        return data_Arr[size][max_val]
    ans = sys.maxsize

    for ind in range(min_Val, max_val + 1):
        x = find_cost(data_Arr, arr, size - 1, ind, min_Val)
        ans = min(ans, x + abs(arr[size - 1] - ind))

    data_Arr[size][max_val] = ans
    return data_Arr[size][max_val]


# Driver Code
arr = [ 5, 4, 3, 2, 1 ]
n = len(arr)
print(find_cost(data_Arr, arr, n, 1, 5))
