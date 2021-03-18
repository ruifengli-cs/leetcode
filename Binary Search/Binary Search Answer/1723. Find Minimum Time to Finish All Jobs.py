# APP1: DFS. idx, workder. each job can be assigned to one of the worker. get all comb and find min max time.
# Time: O(k^n) space: O(n) Runtime: 14%
# Optimization 1:
# we assign the most time consuming work first.

# Optimization 2:
# Assign a work to totally free worker only once.

# Optimization 3:
# Update the res and don't go forward if work load already >= res. because res is global and already udpated
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True) # opt 1
        self.res = sum(jobs)
        workers = [0] * k
        self.dfs(jobs, 0, workers)
        return self.res

    def dfs(self, jobs, idx, workers):
        if idx == len(jobs):
            self.res = min(self.res, max(workers))
            return
        for i in range(len(workers)):
            if workers[i] + jobs[idx] >= self.res:
                continue
            workers[i] += jobs[idx]
            self.dfs(jobs, idx + 1, workers)
            workers[i] -= jobs[idx]
            if workers[i] == 0: # opt 2
                return

# APP2: binary search answer. APP1 upper bound is not reducing quick enough.
# TIme: O(lg(time_sum) * k^n) space: O(n) runtime: 94%
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if not jobs or k <= 0:
            return -1
        n = len(jobs)
        jobs.sort(reverse=True)
        left, right = max(jobs), sum(jobs)
        while left < right:
            mid = (left + right) >> 1
            workers = [mid] * k
            if self.dfs(jobs, 0, workers, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def dfs(self, jobs, idx, workers, mid):
        if idx == len(jobs):
            return True
        for i in range(len(workers)):
            if workers[i] >= jobs[idx]:
                workers[i] -= jobs[idx]
                if self.dfs(jobs, idx + 1, workers, mid):
                    return True
                workers[i] += jobs[idx]
            if workers[i] == mid:
                break
        return False
