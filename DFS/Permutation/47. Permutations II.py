# Solution1:
# dfs + visited set, need sort to remove duplicates
# Time: O(n!) space: O(n) stack, O(n) visited
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        visited = set()
        res = []
        nums.sort()
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, path, res, visited):
        if len(visited) == len(nums):
            res.append(copy.deepcopy(path))
            return
        for i in range(len(nums)):
            if i in visited or (i > 0 and nums[i] == nums[i - 1] and i - 1 in visited):
                continue
            path.append(nums[i])
            visited.add(i)
            self.dfs(nums, path, res, visited)
            visited.remove(i)
            path.pop()

