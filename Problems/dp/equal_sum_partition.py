"""
Model: 0/1 Knapsack Problem 2
GFG Link: https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
Leetcode: https://leetcode.com/problems/partition-equal-subset-sum/
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
"""
Solution: 
Question -  sum(p1) == sum(p2) 
i.e and we know that => s1 + s2 = sum(all_elements in arr)
=> if SUM is odd then always False 
=> SUM(arr) = 2S1 
=> S1 = SUM(arr)/2                       
by this we got S1 value, find the subset with sum as s1 
"""


# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        sum = 0
        for i in arr: sum += i
        if sum % 2 != 0: return False
        sum = int(sum / 2)
        dp = [[0 for i in range(sum + 1)] for j in range(N + 1)]  # dp[N+1][sum+1]
        for i in range(N + 1):
            dp[i][0] = 1
        # print(dp)
        for i in range(1, N+1):
            for j in range(1, sum+1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[N][sum]


#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends


# leetcode Solution:
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         sum = 0
#         N = len(nums)
#         for i in nums: sum += i
#         if sum % 2 != 0: return False
#         sum = int(sum / 2)
#         dp = [[0 for i in range(sum + 1)] for j in range(N + 1)]  # dp[N+1][sum+1]
#         for i in range(N + 1):
#             dp[i][0] = 1
#         # print(dp)
#         for i in range(1, N+1):
#             for j in range(1, sum+1):
#                 if nums[i - 1] <= j:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
#                 else:
#                     dp[i][j] = dp[i - 1][j]
#         # print(dp)
#         return dp[N][sum]
