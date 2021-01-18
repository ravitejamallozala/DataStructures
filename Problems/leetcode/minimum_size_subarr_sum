"""
209. Minimum Size Subarray Sum
Medium
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""
# class Solution:
#     # O(n) Solution Accepted
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         i=0
#         j=0
#         sum = nums[0]
#         min_val = None
#         while i < len(nums) and j < len(nums) and i <= j:
#             # print("i ", i, "j: ", j, "sum ", sum, "min_val:",min_val)
#             if sum >= s:
#                 temp_val = j - i + 1
#                 if not min_val or temp_val < min_val:
#                     min_val = temp_val
#                 # min_val = temp_val if temp_val < min_val else min_val
#                 sum -= nums[i]
#                 i += 1
#             else:
#                 j += 1
#                 if not j<len(nums): break
#                 sum += nums[j]
#         return min_val or 0
class Solution:
    # O(n) Solution Accepted
    def minSubArrayLen(self, s, nums):
        prefixSum = [0]
        for num in nums:
            prefixSum.append(num + prefixSum[-1])

        left, right = 1, len(nums) + 1
        while left < right:
            median = left + (right - left) // 2
            maxVal = max([prefixSum[i] - prefixSum[i - median] for i in range(median, len(prefixSum))])
            if maxVal >= s:
                right = median
            else:
                left = median + 1
        return left if left <= len(nums) else 0

# Driver code
if __name__ == '__main__':
    s = Solution()
    ans = s.minSubArrayLen(7, [2,3,1,2,4,3])
    print(ans)