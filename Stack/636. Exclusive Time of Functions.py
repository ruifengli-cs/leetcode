class Solution:
    # APP1: use stack, store in job is interruptted and interrupted time
    # Time: O(n) Space: O(n) Runtime: 78%
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not n or n < 0 or not logs:
            return []
        res, stack = [0] * n, []
        for log in logs:
            id, status, timestamp = log.split(':')
            if status == "start":
                if stack:
                    stack[-1][2] = True
                stack.append([int(id), int(timestamp), False, 0])
            else:
                s_id, s_timestamp, interrupted, interrupt_time = stack.pop()
                duration = int(timestamp) - s_timestamp + 1
                if interrupted:
                    res[s_id] += duration - interrupt_time
                else:
                    res[s_id] += duration
                if stack:
                    stack[-1][3] += duration
        return res

    # APP2: use stack, prev and cur time to calculate.
    # Time: O(n) Space: (n) only for id Runtime: 97%
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res, stack, prev_t = [0] * n, [], 0
        for log in logs:
            id, status, cur_t = log.split(':')
            cur_t = int(cur_t)
            if status == "start":
                if stack:
                    res[stack[-1]] += cur_t - prev_t
                stack.append(int(id))
                prev_t = cur_t
            else:
                res[stack.pop()] += cur_t - prev_t + 1
                prev_t = cur_t + 1
        return res