# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
        
                in every node we'll have to check the height of left 
                subtree and right subtree, whichever is maximum, return that + 1
                
        if there is only 1 node then the height is 1
        
        """
        
        def findMaxDepth(node):
            if node is None:
                return 0
            
            leftSubtreeHeight = findMaxDepth(node.left)
            rightSubtreeHeight = findMaxDepth(node.right)
            
            return max(leftSubtreeHeight, rightSubtreeHeight) + 1
        
        return findMaxDepth(root)
        