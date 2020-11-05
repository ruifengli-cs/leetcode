class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """

    # APP1: brute force: start with Alice, find all comb. then start with Bob, find all comb.
    # Time: O(n^2) space: O(1)

    # APP2: loop through center line. pre-calculate alice max val and bob max val in O(n)
    # Time: O(n) space: O(n)

    def PickApples(self, Trees, A, B):
        if not Trees or not A or not B:
            return 0
        if A + B > len(Trees):
            return -1
        alice, bob, now_A, now_B, max_A, max_B, n, res = [], [], 0, 0, 0, 0, len(Trees), 0
        for i, tree in enumerate(Trees):
            now_A += tree
            now_B += tree
            max_A = max(max_A, now_A)
            max_B = max(max_B, now_B)
            alice.append(max_A)
            bob.append(max_B)
            if i >= A - 1:
                now_A -= Trees[i - A + 1]
            if i >= B - 1:
                now_B -= Trees[i - B + 1]
        # print(alice)
        now_A = now_B = max_A = max_B = 0
        for i in range(n - 1, -1, -1):
            alice[i] += max_B
            bob[i] += max_A
            res = max(res, alice[i], bob[i])
            # print(i, res, alice[i], now_B, max_B)
            now_A += Trees[i]
            now_B += Trees[i]
            max_A = max(max_A, now_A)
            max_B = max(max_B, now_B)
            if i <= n - A:
                now_A -= Trees[i + A - 1]
            if i <= n - B:
                now_B -= Trees[i + B - 1]
        # print(alice, bob)
        res = max(res, max_A, max_B)
        return res


class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """

    def PickApples(self, A, K, L):

        # write your code here
        n = len(A)
        if K + L > n:
            return -1
        left_A, left_B = self.get_dp(A, K), self.get_dp(A, L)
        temp_num = [A[i] for i in range(len(A) - 1, -1, -1)]
        right_A, right_B = self.get_dp(temp_num, K), self.get_dp(temp_num, L)

        right_A.reverse()
        right_B.reverse()
        ans = -1
        print(left_A, left_B)

        for i in range(n - 1):
            temp_maximum = -1
            if left_A[i] != -1 and right_B[i + 1] != -1:
                temp_maximum = max(temp_maximum, left_A[i] + right_B[i + 1])
            if left_B[i] != -1 and right_A[i + 1] != -1:
                temp_maximum = max(temp_maximum, left_B[i] + right_A[i + 1])
            ans = max(ans, temp_maximum)

        return ans

    def get_dp(self, nums, limit):
        arr_sum, index, result = sum(nums[:limit]), limit, [-1] * len(nums)

        result[limit - 1] = arr_sum
        while index < len(nums):
            arr_sum = arr_sum + nums[index] - nums[index - limit]
            result[index] = max(result[index - 1], arr_sum)
            index += 1
            return result
