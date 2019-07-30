'''
Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set()
        result = set()
        for i in nums1:
            s.add(i)
        for i in nums2:
            if i in s:
                result.add(i)
        return list(result)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
sol = Solution()
print(sol.intersection(nums1, nums2))
