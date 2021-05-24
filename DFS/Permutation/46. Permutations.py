# APP1: dfs pick or not pick
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        visited = set()
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(visited) == len(nums):
            res.append(copy.deepcopy(path))
            return
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            path.append(nums[i])
            visited.add(nums[i])
            self.dfs(nums, visited, path, res)
            visited.remove(nums[i])
            path.pop()