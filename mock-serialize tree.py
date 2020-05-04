# #Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.#

#         1
#       /  \
#      2    3
#     /     /\
#    4     5  6
#     \
#      7
# # Serialize: 1, 2, 3, 4, #, 5, 6, # ,7
# # Deserialize: reconstruct back the original tree

# Output：{3,9,20,#,#,15,7}
# Explanation：
# Binary tree {3,9,20,#,#,15,7},  denote the following structure:
#       3
#      / \
#     9  20
#       /  \
#      15   7
# it will be serialized {3,9,20,#,#,15,7}
    

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# Serialize:           
# APProach1                       
# BFS to traverse through the tree. add node the the queue. if it's leaf node, don't add anything. 
# If it has either left or right child, add the other empty as #                      

# Approach2:
# dfs pre-order traverse: 1,2,4,#,7,#,#,#,3,5,#,#,6,#,#,
# Deserialize: [1,2,4,#,7,#,#,#,3,5,#,#,6,#,#]
            # 1                  [2,4,#,7,#,#,#,3,5,#,#,6,#,#]
           # /
#          2                        [4,#,7,#,#,#,3,5,#,#,6,#,#]
#        /
      # 4               [#,7,#,#,#,3,5,#,#,6,#,#]
     #    \     
  #        7    [#,#,3,5,#,#,6,#,#]
                 # [3,5,#,#,6,#,#]
import collections
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        return self.in_order(root, "")
        
    def in_order(self, root, serialized_str):
        if root is None:
            serialized_str += "#,"
            return serialized_str
        serialized_str += str(root.val) + ','
        serialized_str = self.in_order(root.left, serialized_str)
        serialized_str = self.in_order(root.right, serialized_str)
        return serialized_str
        
                
                      
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        data = data.split(',')
        q = collections.deque(data)
        root = self.dfs(q)
        return root
    
    def dfs(self, q):
        if q and q[0] == '#':
            q.popleft()
            return
        
        root = TreeNode(q[0])
        q.popleft()
        root.left = self.dfs(q)
        root.right = self.dfs(q)
        return root
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(7)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
sol = Solution()
print(sol.serialize(root))
