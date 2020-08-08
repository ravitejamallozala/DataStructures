
"""
AUG 1
 Detect Capital

Solution
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = False
        double_caps = False
        lower = False
        for s in word:
            if s.isupper():
                if caps:
                    double_caps = True
                caps = True
                if lower:
                    return False
            else:
                lower = True
                if double_caps:
                    return False

        return True