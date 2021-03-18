# APP1: find all comb fo words, loop through s to find if it's in combs.
# Time: O(m^2 * k + nmk) space: O(m^2 * k), k = len(word), n = len(s), m = len(words) Runtime: TLE
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        combs, visited = set(), set()
        self.form_combs(words, combs, [], visited)
        k, n, res = len(words[0]) * len(words), len(s), []
        for i in range(n - k + 1):
            if s[i:i + k] in combs:
                res.append(i)
        return res

    def form_combs(self, words, combs, path, visited):
        if len(visited) == len(words):
            path_str = ''.join(path)
            combs.add(path_str)
        length = 0
        for i in range(len(words)):
            if i not in visited:
                path.append(words[i])
                visited.add(i)
                self.form_combs(words, combs, path, visited)
                path.pop()
                visited.remove(i)

# APP2: two hash as sliding window. since words length are equal, divide first k chars into k parts as starting point.
# Time: O(k * n) space: O(mk) Runtime: 94%
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        whash, k, n, m, res = {}, len(words[0]), len(s), len(words), []
        # init
        for word in words:
            whash[word] = whash.get(word, 0) + 1

        # divide first word into k parts.
        for i in range(k):
            window, wcount = {}, 0
            for j in range(i, n, k):
                word = s[j: j + k]
                if word in whash:
                    window[word] = window.get(word, 0) + 1
                    wcount += 1

                    while window[word] > whash[word]:
                        pos = j - k * (wcount - 1)
                        remove_word = s[pos: pos + k]
                        window[remove_word] -= 1
                        wcount -= 1
                else:
                    window.clear()
                    wcount = 0
                if wcount == m:
                    res.append(j - k * (m - 1))
        return res
