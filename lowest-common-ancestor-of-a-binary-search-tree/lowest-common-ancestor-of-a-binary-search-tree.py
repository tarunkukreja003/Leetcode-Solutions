# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfsRecursiveLCA(currNode):
            
            if (p.val <= currNode.val and currNode.val <= q.val) or (q.val <= currNode.val and currNode.val <= p.val):
                return currNode
            elif (p.val < currNode.val and q.val < currNode.val):
                return dfsRecursiveLCA(currNode.left)
            
            elif (p.val > currNode.val and q.val > currNode.val):
                return dfsRecursiveLCA(currNode.right)
            
        return dfsRecursiveLCA(root)