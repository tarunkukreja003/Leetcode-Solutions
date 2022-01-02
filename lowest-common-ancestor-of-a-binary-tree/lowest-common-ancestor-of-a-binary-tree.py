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
        
        # time complexity - O(n)
        # space complexity - O(n) - because of recursion stack
        
        def findLCA(node):
            if node is None:
                return 
            if node is p or node is q:
                return node
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            if left and right:
                return node
            
            return left or right
            
        
        return findLCA(root)
            
        
        
        
        
        
        