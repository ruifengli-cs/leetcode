IS_WORD = '#'


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node[IS_WORD] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.trie
        return self.dfs(word, 0, len(word), node)

    def dfs(self, word, i, n, node):
        # since i'm loop through all the keys, need to check '#'
        if node == True:
            return False
        if i == n:
            return True if IS_WORD in node else False

        ch = word[i]
        if ch != '.':
            if ch not in node:
                return False
            return self.dfs(word, i + 1, n, node[ch])

        for ch in node.keys():
            if self.dfs(word, i + 1, n, node[ch]):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)