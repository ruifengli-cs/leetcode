class Solution:
    # APP1: dfs recurssion: min step from 0 to end = 1 + min(reachable pos to end)
    # Time: O(max_step ^ n) space: O(n) stack Runtime: TLE
    #     def jump(self, nums: List[int]) -> int:
    #         if not nums:
    #             return 0
    #         return self.dfs(nums, 0)

    #     def dfs(self, nums, i):
    #         if i >= len(nums) - 1:
    #             return 0
    #         min_step = sys.maxsize
    #         for j in range(1, nums[i] + 1):
    #             min_step = min(min_step, self.dfs(nums, i + j))
    #         return min_step + 1

    # APP2: bfs + visited dict, when fist reach last pos, return step.
    # Time: O(n) space: O(n) Runtime: TLE
    #     def jump(self, nums: List[int]) -> int:
    #         if not nums or len(nums) < 2:
    #             return 0
    #         q, visited = collections.deque([0]), {0: 0}
    #         while q:
    #             idx = q.popleft()
    #             for i in range(1, nums[idx] + 1):
    #                 new_idx = idx + i
    #                 if new_idx >= len(nums) - 1:
    #                     return visited[idx] + 1
    #                 if new_idx not in visited:
    #                     visited[new_idx] = visited[idx] + 1
    #                     q.append(new_idx)

    # APP3: greedy: cur_step_max: cur max pos this step can reach, max_pos: max pos it can reach by far
    # when cur > cur_step_max, step += 1, cur_step_max = max_pos
    # Time: O(n) space: O(1)
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        cur_step_max = max_pos = steps = 0
        for i in range(len(nums)):
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= len(nums) - 1:
                return steps + 1
            if i == cur_step_max:
                steps += 1
                cur_step_max = max_pos



