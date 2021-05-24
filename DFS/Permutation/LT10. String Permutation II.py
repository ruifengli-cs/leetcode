class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        res = []
        if str is None:
            return res
        s = sorted(str)
        visited = [False] * len(s)
        self.dfs(s, visited, [], res)
        return res

    def dfs(self, s, visited, perm, res):
        if len(perm) == len(s):
            res.append("".join(perm))
            return

        for i in range(len(s)):
            if visited[i]:
                continue
            if i > 0 and s[i] == s[i - 1] and visited[i - 1] == False:
                continue

            perm.append(s[i])
            visited[i] = True
            self.dfs(s, visited, perm, res)
            visited[i] = False
            perm.pop()

    # Treat as string
    # def stringPermutation2(self, str):
    #     # write your code here
    #     res = []
    #     if str is None:
    #         return res
    #     visited = [False] * len(str)

    #     str = "".join(sorted(str))
    #     self.dfs(str, visited, "", res)
    #     return res

    # def dfs(self, A, visited, perm, A_perms):
    #     if len(perm) == len(A):
    #         A_perms.append(perm)
    #         return

    #     for i in range(len(A)):
    #         if visited[i]:
    #             continue
    #         if i > 0 and A[i] == A[i - 1] and visited[i - 1] == False:
    #             continue

    #         perm += A[i]
    #         visited[i] = True
    #         self.dfs(A, visited, perm, A_perms)
    #         visited[i] = False
    #         perm = perm[: -1]