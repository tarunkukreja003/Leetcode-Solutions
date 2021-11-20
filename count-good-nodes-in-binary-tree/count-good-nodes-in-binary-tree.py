# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numberOfGoodNodes = 0
        
        def travrseTree(root, maxAncestorVal):
            
            if root == None:
                return
            
            
            if root.val >= maxAncestorVal:
                self.numberOfGoodNodes += 1
                maxAncestorVal = root.val
            
            travrseTree(root.left, maxAncestorVal)
            travrseTree(root.right, maxAncestorVal)
        
        travrseTree(root, float('-inf'))
        
        return self.numberOfGoodNodes
        