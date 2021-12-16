# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we have to find where it is violating the property of BST
        
        # the current node should be between left value and right value
        def recursiveValidateBST(node, leftValue, rightValue):
            if not node:
                return True
            if node.val <= leftValue or node.val >= rightValue:
                return False
            
            return recursiveValidateBST(node.right, node.val, rightValue) and recursiveValidateBST(node.left, leftValue, node.val)
            
            
            
            
            
            
            
            
            
        
        return recursiveValidateBST(root, float('-inf'), float('inf'))
            
            