# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def findMinDepth(node):
            if node is None:
                return 0
            
            leftSubtreeHeight = findMinDepth(node.left)
            rightSubtreeHeight = findMinDepth(node.right)
            
            if leftSubtreeHeight == 0 and rightSubtreeHeight == 0:
                # leaf node
                return 1
            elif leftSubtreeHeight == 0 and rightSubtreeHeight != 0:
                # the leaf node is in the right subtree
                return rightSubtreeHeight + 1
            elif leftSubtreeHeight != 0 and rightSubtreeHeight == 0:
                # the leaf node is in the left subtree
                return leftSubtreeHeight + 1
            else:
                return min(leftSubtreeHeight, rightSubtreeHeight) + 1
        
        return findMinDepth(root)
        