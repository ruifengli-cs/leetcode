# APP1: BFS from end to start word, store prev node info in a dict.
# DFS from start to end
# Time: O(n*26*n) for BFS, O(26^n) for dfs.
# where n: average word length, N: number of words. check if word in dict takes O(n)
# Space: O(n*26)
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        if len(beginWord) != len(endWord):
            return res
        words = set(wordList)
        visited = self.bfs(beginWord, endWord, wordList, words)

        seen = set([beginWord])
        self.dfs(beginWord, endWord, visited, seen, [beginWord], res, words)
        return res

    def dfs(self, cur, endWord, visited, seen, path, res, words):
        if cur == endWord:
            res.append(copy.deepcopy(path))
            return
        for i in range(len(cur)):
            for ch in "qwertyuiopasdfghjklzxcvbnm":
                newword = cur[:i] + ch + cur[i + 1:]
                if newword not in seen and newword in words and visited[newword] == visited[cur] - 1:
                    seen.add(newword)
                    path.append(newword)
                    self.dfs(newword, endWord, visited, seen, path, res, words)
                    path.pop()
                    seen.remove(newword)

    def bfs(self, beginWord, endWord, wordList, words):
        visited = {endWord: 0}
        q = collections.deque([endWord])

        words.add(beginWord)
        while q:
            word = q.popleft()
            for i in range(len(word)):
                for ch in "qwertyuiopasdfghjklzxcvbnm":
                    newword = word[:i] + ch + word[i + 1:]
                    if newword in words and newword not in visited:
                        q.append(newword)
                        visited[newword] = visited[word] + 1
        return visited

