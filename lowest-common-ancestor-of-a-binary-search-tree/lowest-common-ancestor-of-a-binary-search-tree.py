# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # can p and q be the same? - no
        # since its a BST - any 2 elements can't be same right? - correct
        # if p is a parent of q or vica-versa then parent will be returned
        
        
        # if p.val > q.val then p can be the ancestor or the ancestro is between them
        # write the code to find the LCA between the 2
        
        # if the curr Node is in between p and q or equal to either then thats the LCA
        def recursiveFindLCA(currNode, p, q):
            if currNode == None:
                return
            
            
            if (currNode.val >= q.val and currNode.val <= p.val) or (currNode.val <= q.val and currNode.val >= p.val):
                    # currNode is the ancestor
                return currNode
            
            elif p.val > currNode.val and q.val > currNode.val:
                return recursiveFindLCA(currNode.right, p, q) 
            
            elif p.val < currNode.val and q.val < currNode.val:
                return recursiveFindLCA(currNode.left, p, q) 
            
            
            
            
        
        return recursiveFindLCA(root, p, q)
            
        