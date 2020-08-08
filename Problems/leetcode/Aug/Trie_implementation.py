"""
 Add and Search Word - Data structure design
 AUG Week 1
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class Trie:
    def __init__(self):
        self.is_leaf = False
        self.child = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        trie = {
            "c": { is_leaf: False, child: {"a":{is_leaf=False, child:{"t": is_leaf:True, child:{}} }}}
        }
        """

        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.trie
        for letter in word:
            if letter in temp.child:
                temp = temp.child.get(letter)
            else:
                t = Trie()
                temp.child[letter] = t
                temp = temp.child.get(letter)
        temp.is_leaf = True

    def search_regex(self, word, trie_node):
        if not trie_node:
            return False
        if len(word) < 1:
            return trie_node.is_leaf
        if word[0] is ".":
            ans = False
            for key in trie_node.child.keys():
                ans = ans or self.search_regex(word[1:], trie_node.child.get(key))
            return ans
        elif word[0] in trie_node.child:
            return self.search_regex(word[1:], trie_node.child.get(word[0]))
        else:
            return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        temp = self.trie
        count = 0
        for letter in word:
            count += 1
            if letter is ".":
                ans = False
                for key in temp.child.keys():
                    ans = ans or self.search_regex(word[count:], temp.child.get(key))
                return ans
            elif letter in temp.child:
                temp = temp.child.get(letter)
            else:
                return False
        if temp.is_leaf is True:
            return True
        return False


# Driver code
if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")
    print(obj.search("."))  # -> true
    print(obj.search("a"))  # -> true
    print(obj.search("aa"))  # -> false
    print(obj.search("a"))  # -> true
    print(obj.search(".a"))  # -> false
    print(obj.search("a."))  # -> false
    # obj.addWord("mad")
    # obj.addWord("bafs")
    # obj.addWord("mad")
    # ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search"]
    # [[], ["a"], ["a"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]
    # print(obj.search("a"))  # -> false
    # print(obj.search("a"))  # -> true
    # print(obj.search(".ad"))  # -> true
    # print(obj.search("b.."))  # -> true
