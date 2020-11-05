class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """

    def shortestSubarray(self, A, K):
        if not A or K is None:
            return 0
        presum, q, nowsum, n, res = [0], collections.deque(), 0, len(A), sys.maxsize

        # get prefix sum
        for num in A:
            nowsum += num
            presum.append(nowsum)

        for i in range(n + 1):
            while q and presum[i] <= presum[q[-1]]:
                q.pop()
            q.append(i)
            while q and presum[q[-1]] - presum[q[0]] >= K:
                res = min(res, i - q.popleft())
        return res if res != sys.maxsize else -1