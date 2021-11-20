# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # it has to be the path between 2 leaf nodes
        # dfs
        # for every node we'll calculate the longest path in the left subtree and longest path of right subtree
        # longestPath(left)
        # longestPath(right)
        
        self.diameter = 0
        
        def longestPath(root):
            if root == None:
                return 0
            
            longestPathLeft = longestPath(root.left)
            longestPathRight = longestPath(root.right)
            
            self.diameter = max(self.diameter, longestPathLeft + longestPathRight)
            
            return max(longestPathLeft, longestPathRight) + 1
        
        
        longestPath(root)
            
        return self.diameter
        