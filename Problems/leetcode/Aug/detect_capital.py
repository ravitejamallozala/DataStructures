# leetcode
# AUG 1
# Detect Capital

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