# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursiveTree(root):
            if root == None:
                return
                
            
            # if (root.left != None) and (root.right != None):
            root.left, root.right = root.right, root.left
            
            recursiveTree(root.left)
            recursiveTree(root.right)
            return root
        
        return recursiveTree(root)
            
            
        