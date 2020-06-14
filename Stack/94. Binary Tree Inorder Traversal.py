# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # APP1: Recursion. Time: O(n), space: O(H)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.in_order(root, res)
        return res

    def in_order(self, root, res):
        if not root:
            return
        self.in_order(root.left, res)
        res.append(root.val)
        self.in_order(root.right, res)

    # APP2: iteration
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                res.append(stack[-1].val)
        return res