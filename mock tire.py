# design a data structure that supports the following two operations:
# 1. addWord(word: str) return None
# 2. search(word: str) -> return True or False

# input to search may contain '.', which is  any one letter
# all words are only lower case.

# 'ad.' = 'ad(a-z)'

# add, adault
# Trie
#              ' '
#              /
#             abcd....
#            /\
#           d
#          / \
#         d   a
#              \
#               u
#               \
#                l
#                 \
#                  t
# 1. Define TrieNode: children -> defaultdict of TrieNode, is_word -> bool, val
# 2. addWord: get root, add each char from the word to Trie, then set is_word=True for last node
# 3. search: dfs each char from the word

# n = len(word)
# Time: add: O(n) search: O(26 ^ n) Space: O(26 ^ Max(len(word)))
import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Solution():
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word) -> bool:
        node = self.root
        self.find_word = False
        self.dfs(node, word, 0)
        return self.find_word

    def dfs(self, node, word, idx) -> bool:
        if idx == len(word):
            if node.is_word:
                self.find_word = True
            return
        if word[idx] == '.':
            for child in node.children.values():
                self.dfs(child, word, idx + 1)
        else:
            child = node.children.get(word[idx])
            if child:
                self.dfs(child, word, idx + 1)


sol = Solution()
sol.addWord("add")
sol.addWord("apple")
print(sol.search("ap..e"))