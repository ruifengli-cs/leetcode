class Solution:
    # APP1: DFS, create new string each time
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        ans = []
        self.dfs(n, n, "", ans)
        return ans

    def dfs(self, left, right, path, ans):
        if left == 0 and right == 0:
            ans.append(path)
        if right < left:
            return
        if left > 0:
            self.dfs(left - 1, right, path + '(', ans)
        if right > 0:
            self.dfs(left, right - 1, path + ')', ans)

    # APP2: DFS backtracking, each step add either left or right. Runtime: 99%
    def generateParenthesis(self, n: int) -> List[str]:
        if not n or n < 1:
            return []
        res = []
        self.dfs(n, 0, 0, [], res)
        return res

    def dfs(self, n, left, right, path, res):
        if right > left or left > n or right > n:
            return
        if left == n and right == n:
            res.append("".join(path))
            return
        path.append('(')
        self.dfs(n, left + 1, right, path, res)
        path.pop()
        path.append(')')
        self.dfs(n, left, right + 1, path, res)
        path.pop()