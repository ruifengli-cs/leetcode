# question: 
# input: Treenode: root, also I have two nodes in the tree. Find their lowest common ancester. 

     #     2
     #    / \
     #   3.  4
     #  / \ / \
     # 5. 6 7 8
    
# LCA of 5 and 6: 3
#       5 and 3: 3
#       5 and 8: 2
      # 2 and 4:    5, 6
# no parent pointer
# approach: dfs, divide and conquer
# dfs defination: return me the LCA
# left = self.dfs(root.left)
# right = self.dfs(root.right)
# 1. two nodes are on the same side
# 2. two nodes are split, one on left, one on right
# 3. one node is the root
# 4. both left and right are none

# 1, LCA on left or right -> return LCA
# 2&3: didn't find LCA on left or right. I will return the node itself

class Solution:
    def find_lca(self, root, node1, node2):
        if root is None:
            return None
        
        if root == node1 or root == node2:
            return root
        
        left = self.find_lca(root.left, node1, node2)
        right = self.find_lca(root.right, node1, node2)
        
#       find lca on both -> return root
        if left and right:
            return root
    
#       find lca on ethier side 
        if left:
            return left
        if right:
            return right
        
        return None

class TreeNode:
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None
        
root_node = TreeNode(2)
root_node.left = TreeNode(3)
root_node.left.left = TreeNode(5)
root_node.left.right = TreeNode(6)
root_node.right = TreeNode(4)
root_node.right.left = TreeNode(7)
root_node.right.right = TreeNode(8)

sol = Solution()
res = sol.find_lca(root_node, root_node.left.left, root_node.right.right)
print(res.val)
# test case 1: 2, 5, 6   
# root, left, right
# 5       N    N  
# 6       N.   N
# 3       5.   6
# 2.      3    N
# ans: 3

# test case 2: 2, 3, 5 
# root, left, right
# 5       N    N  
# 6       N.   N
# 3      5.    N
# 2       3.   N
# ans 3
