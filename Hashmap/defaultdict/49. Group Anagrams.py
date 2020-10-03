class Solution:
    # APP0 (NOT WORKING): for each str, get it's counter, then use counter as key to put it in defaultdict. It won't work because counter is unhashable.
    # APP1: Brute force. compare str with all others to check if they're anagram.
    # Time: O(n^2) space: O(n) Runtime: TLE
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res, n, visited = [], len(strs), set()
        for i in range(n):
            if i not in visited:
                subset = self.get_anagrams(strs, i, visited)
                res.append(subset)
        return res

    def get_anagrams(self, strs, i, visited):
        subset, count_i = [strs[i]], collections.Counter(strs[i])
        visited.add(i)
        for j in range(i + 1, len(strs)):
            if j not in visited and collections.Counter(strs[j]) == count_i:
                subset.append(strs[j])
                visited.add(j)
        return subset

    # APP2: base on same idea of APP0, use array of 26 as counter. tuple(array) is hashbable
    # Time: O(n) Space: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res, data = [], collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            data[tuple(count)].append(word)
        for _, group in data.items():
            res.append(group)
        return res