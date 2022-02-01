# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, a, b):
        if not b:
            return True
        
        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
        
        def dfs(s, t):
            if not s:
                return False
            
            if s.val == t.val and checkTree(s, t):
                return True
            
            return dfs(s.left, t) or dfs(s.right, t)
            
        return dfs(a, b)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        """
        
        isIdentical(root, subRoot):
            
            if root.val == subRoot.val and isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)
        
        
        travel down the tree until we find val = subroot.val
        
        after finding the node traverse both the trees simultaneously, if any node is not equal then return and travel in the tree to find another subroot
        
        if subroot has reached none and root has not or vica-versa then return False
        
        
        
        
        
        
        
            
        
        """
        
        def findSubrootVal(node, subNode):
            if not node:
                return False
                
            if node.val == subNode.val and isMatch(node, subNode):
                return True
                
            
            return findSubrootVal(node.left, subNode) or findSubrootVal(node.right, subNode)
        
        def isMatch(node, subNode):
            if not node and not subNode:
                return True
            
            if (not node and subNode) or (not subNode and node):
                return False
            
            if node.val != subNode.val:
                return False
            
            return isMatch(node.right, subNode.right) and isMatch(node.left, subNode.left)
        
        return findSubrootVal(root, subRoot)
                