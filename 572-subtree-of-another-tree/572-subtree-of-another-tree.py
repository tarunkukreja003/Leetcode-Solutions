# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        """
        
        
        travel down the tree until we find val = subroot.val
        
        after finding the node traverse both the trees simultaneously, if any node is not equal then return false and travel further down in the tree to find another subroot
        
        if subroot has reached none and root has not or vica-versa then return False
        
        
        
        
        
        
        
            
        
        """
        
        def findSubrootVal(node, subRoot):
            if node is None:
                return False
                
            if node.val == subRoot.val and isMatch(node, subRoot):
                return True
                
            
            return findSubrootVal(node.left, subRoot) or findSubrootVal(node.right, subRoot)
        
        def isMatch(node, subNode):
            if node is None and subNode is None:
                return True
            
            if (not node and subNode) or (not subNode and node):
                return False
            
            if node.val != subNode.val:
                return False
            
            return isMatch(node.right, subNode.right) and isMatch(node.left, subNode.left)
        
        return findSubrootVal(root, subRoot)
                