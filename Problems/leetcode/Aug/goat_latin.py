"""
Goat Latin

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        ans = ""
        aes = 'a'
        for word in S.split():
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma' + aes
            aes += 'a'
            ans += ' ' + word
        # print(ans)
        return ans.strip()
        # return ' '.join((w if w[0].lower() in "aeiou" else w[1:]+w[0]) + 'maa' + 'a'*i for i, w in enumerate(S.split(' ')))


# Driver code:
if __name__ == '__main__':
    s = Solution()
    sen = "I speak Goat Latin"
    ans = s.toGoatLatin(sen)
    print(ans)
