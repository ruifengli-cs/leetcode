class Solution:
    # APP1: BFS for each idx, swith to another ch in 26 chars, add valid into queue.
    # Time: O(n^2 * N) Space: O(nN)?
    # n = len(word), N = total words
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or len(beginWord) != len(endWord):
            return 0
        q = collections.deque([beginWord])
        visited = {beginWord: 1}
        dictionary = set(wordList)
        while q:
            word = q.popleft()
            if word == endWord:
                return visited[word]
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word not in visited and new_word in dictionary:
                        q.append(new_word)
                        visited[new_word] = visited[word] + 1
        return 0
