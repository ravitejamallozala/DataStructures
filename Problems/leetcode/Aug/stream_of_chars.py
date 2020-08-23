"""
Stream of Characters

Solution
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.


Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist


Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
   Hide Hint #1
Put the words into a trie, and manage a set of pointers within that trie.
"""
class Trie:
    def __init__(self, is_leaf):
        """
        { element : {val : 1, is_end: False}]}

       """
        self.is_leaf = is_leaf
        self.child = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        # print("its here")
        self.trie = {}
        self.max_length = 0
        self.word = ""
        for word in words:
            self.max_length = len(word) if len(word) > self.max_length else self.max_length
            self.insert_word(word)

    def query(self, letter: str) -> bool:
        self.word += letter
        self.word = self.word[-self.max_length:] if len(self.word) > self.max_length else self.word
        ans = self.search_word()
        return ans

    def insert_word(self, word):
        head = self.trie
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in head:
                t = Trie(True) if i == 0 else Trie(False)
                head[word[i]] = t
                head = t.child
            else:
                node = head.get(word[i])
                if i == 0:
                    node.is_leaf = True
                head = node.child

                # print(head)

    def search_word(self):
        # print("searching ", self.word)
        head = self.trie
        # print(head)
        node = None
        for i in range(len(self.word) - 1, -1, -1):
            # print("letter ", self.word[i])
            if self.word[i] in head:
                node = head.get(self.word[i])
                head = node.child
                if node.is_leaf:
                    return True
            else:
                return False
        return node.is_leaf

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)