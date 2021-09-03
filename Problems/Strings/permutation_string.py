"""
567. Permutation in String
Medium
Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def compare_dicts(self, source, dest):
        # print("search dicts ", source, dest)
        if not len(source.keys()) == len(dest.keys()): return False
        for ind, (key, val) in enumerate(source.items()):
            # print("key:", key , "val ",val)
            if not key in dest or val != dest[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # populating s1_dict
        s1_dict = {}
        for c in s1:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1
        s2_dict = {}
        for i in range(len(s1)):
            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1
            else:
                s2_dict[s2[i]] = 1
        # print(s2_dict)
        j = 0
        while i < len(s2):
            result = self.compare_dicts(s1_dict, s2_dict)
            # print(result)
            if result:
                return True
            if s2[j] in s2_dict:
                s2_dict[s2[j]] -= 1
                if s2_dict[s2[j]] == 0:
                    del s2_dict[s2[j]]
            j += 1
            i += 1
            if not i < len(s2): continue
            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1
            else:
                s2_dict[s2[i]] = 1

        return False
