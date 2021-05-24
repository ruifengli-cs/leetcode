# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum, single_sum = self.dfs(root)
        return max_sum

    def dfs(self, root):
        if root is None:
            return -sys.maxsize, 0
        left_max_sum, left_single_sum = self.dfs(root.left)
        right_max_sum, right_single_sum = self.dfs(root.right)
        root_single_sum = max(left_single_sum, right_single_sum) + root.val
        if root_single_sum < 0:
            root_single_sum = 0
        root_sum = max(left_max_sum, right_max_sum, left_single_sum + right_single_sum + root.val)
        return root_sum, root_single_sum