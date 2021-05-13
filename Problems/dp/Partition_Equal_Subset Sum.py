"""
GFG: Partition Equal Subset Sum
Medium Accuracy: 38.0% Submissions: 40459 Points: 4
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination:
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explaination: This array can never be
partitioned into two such parts.

Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.


Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)


Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000

"""


class Solution:
    """
Main logic:-
    sum1 => sum of partition1
    sum2 => sum of partition2
    sum1 + sum2 = Sumofarr (we also want that sum1 & sum2 should be equal)
    2Sum = sum_or_arr
    sum1 = sumofarr/2
    => Problem is now reduced to find the subset of the array if its sum is sum_of_arr/2
        if there exists a subset then we can say that we can partition this array
    reference link: https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=8
    """

    def dp(self, N, arr, sum_val):
        dp_arr = [[False for j in range(sum_val + 1)] for i in range(N + 1)]
        # intialising Array
        # N =0 -> False, Sum = 0 True
        for i in range(N + 1):
            for j in range(sum_val):
                if j == 0:
                    dp_arr[i][j] = True
                    continue
        for i in range(1, N + 1):
            for j in range(1, sum_val + 1):
                # i value represents the array size -> number of elements in the array for current iteration
                # if i is 3 the we  are considering the array = [1,5,11]
                # similarly for j value if j=3 then sum_val is 3 => sub problem => arr = [1,5,11] & sum = 3
                if arr[i - 1] <= j:
                    dp_arr[i][j] = dp_arr[i - 1][j - arr[i - 1]] or dp_arr[i - 1][j]
                else:
                    dp_arr[i][j] = dp_arr[i - 1][j]
        # print(self.dp_arr)
        return dp_arr[N][sum_val]

    def equalPartition(self, N, arr):
        sum_val = 0
        for i in arr:
            sum_val += i
        if sum_val % 2 != 0:
            return False
        return self.dp(N, arr, sum_val // 2)


# {
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    N = 4
    arr = [1, 5, 11, 5]
    ob = Solution()
    if (ob.equalPartition(N, arr) == 1):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
