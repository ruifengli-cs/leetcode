# APP1: For each candidate, we can pick or not pick. dfs
# Time: O(2^n) space: O(n) stack Runtime: TLE

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = set()
#         candidates.sort()
#         self.dfs(candidates, target, 0, 0, [], res)
#         return res

#     def dfs(self, candi, target, idx, total, seq, res):
#         if idx == len(candi) and total == target:
#             res.add(copy.deepcopy(tuple(seq)))
#             return

#         if total > target or idx == len(candi):
#             return
#         # not pick
#         self.dfs(candi, target, idx + 1, total, seq, res)

#         # pick
#         seq.append(candi[idx])
#         self.dfs(candi, target, idx + 1, total + candi[idx], seq, res)
#         seq.pop()


# APP2: dfs + memoization. idx and sum is the state.
# Time: O(n^2) space: O(n) Runtime: 37%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candi, target, idx, seq, res):
        if target == 0:
            res.append(copy.deepcopy(seq))
            return

        if target < 0 or idx == len(candi):
            return
        # pick
        for i in range(idx, len(candi)):
            if i != idx and candi[i] == candi[i - 1]:
                continue
            seq.append(candi[i])
            self.dfs(candi, target - candi[i], i + 1, seq, res)
            seq.pop()