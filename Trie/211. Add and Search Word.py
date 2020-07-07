class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.is_word = '#'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.is_word] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, 0, self.root)

    def dfs(self, word: str, idx: int, node: dict) -> bool:
        if node == '#':
            return False
        if idx == len(word):
            return True if self.is_word in node else False
        res, ch = False, word[idx]
        if ch == '.':
            for key, val in node.items():
                res = res or self.dfs(word, idx + 1, val)
            return res

        if ch not in node:
            return False

        return self.dfs(word, idx + 1, node[ch])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)