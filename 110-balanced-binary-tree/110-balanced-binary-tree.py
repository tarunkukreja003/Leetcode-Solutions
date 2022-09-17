# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        if there is no nodes then ? balanced -> true
        if there is 1 node then also -> yes
        
        """
        
        def findDepth(node):
            if node is None:
                return 0
            
            leftSubtreeHeight = findDepth(node.left)
            rightSubtreeHeight = findDepth(node.right)
            
            return max(leftSubtreeHeight, rightSubtreeHeight) + 1
        
        def isBalancedBinaryTree(node):
            if node is None:
                return True
            leftSubtreeHeight = findDepth(node.left)
            rightSubtreeHeight = findDepth(node.right)
            
            if (leftSubtreeHeight > rightSubtreeHeight + 1) or (rightSubtreeHeight > leftSubtreeHeight + 1):
                return False
            else:
                return (isBalancedBinaryTree(node.left)) and (isBalancedBinaryTree(node.right))
        
        return isBalancedBinaryTree(root)
            
            
                            
        