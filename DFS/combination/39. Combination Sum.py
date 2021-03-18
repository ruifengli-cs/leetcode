# APP1: dfs. each time pick one chandidate
# Time: O(n * (target // min(candidates))) space: O(n) stack

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candi, idx, target, seq, res):
        if idx == len(candi) and target == 0:
            res.append(copy.deepcopy(seq))
            return
        if target < 0 or idx >= len(candi):
            return
        limit = target // candi[idx]
        for i in range(limit + 1):
            seq.extend([candi[idx]] * i)
            self.dfs(candi, idx + 1, target - i * candi[idx], seq, res)
            for _ in range(i):
                seq.pop()


# APP2: dfs using for loop on index
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, idx, path, res):
        if target == 0:
            res.append(copy.deepcopy(path))
            return
        if target < 0:
            return
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, target - nums[i], i, path, res)
            path.pop()
