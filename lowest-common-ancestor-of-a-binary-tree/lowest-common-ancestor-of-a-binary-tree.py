# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # are all nodes values unique? - yes
        # can p and q be the same? - no
        
        # we'll search in the tree for p and q, and we'll store the node values in a set
        # if we find either p or q we'll break and we'll start from the root again
        # now we'll search for p if q was found previously and vica-versa and we'll check while traversing whether the node is in set or not, if it is not then return its ancestor
        
        # but this algorithm takes space - O(n)
        
        # improved code
        
        # we'll search for both p and q, if we find either of them, we return them back to the parent
        # the basic idea is that if the currNode left and right is not null then return currNode 
        # if the left is null and the right is not then just return the value from right and vica-versa 
        # once we reach the root, it will return the not null subtree value
        
        def findLCA(node, n1, n2):
            if node is None:
                return 
            if node.val == n1.val or node.val == n2.val:
                return node
            
            left = findLCA(node.left, n1, n2)
            right = findLCA(node.right, n1, n2)
            
            if (left is None) and (right is None):
                return
            elif (left is not None) and (right is not None):
                return node
            elif (left is not None) and (right is None):
                return left
            elif (left is None) and (right is not None):
                return right
        
        return findLCA(root, p, q)
            
        
        
        
        
        
        