# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # APP1: do in-order traversal and make sure cur node is not larger than previous node
    # TIme: O(n) space: O(lgn) Runtime: 94%
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.prev = -sys.maxsize
        return self.dfs(root)

    def dfs(self, root: TreeNode):
        if not root:
            return True
        if not self.dfs(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.dfs(root.right)

    # APP2: recursion to return is_bst, left_max, right_min
    # Time: O(n) space: O(lgn) stack runtime: 67%
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        is_bst, _, _ = self.dfs(root)
        return is_bst

    def dfs(self, root):
        if not root:
            return True, -sys.maxsize, sys.maxsize
        is_bst_left, left_max, left_min = self.dfs(root.left)
        is_bst_right, right_max, right_min = self.dfs(root.right)
        if not is_bst_left or not is_bst_right or root.val <= left_max or root.val >= right_min:
            return False, 0, 0
        return True, max(root.val, right_max), min(root.val, left_min)

    # APP3: iteration. BST inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack, cur, prev = [], root, -sys.maxsize
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= prev:
                return False
            prev = cur.val
            cur = cur.right
        return True